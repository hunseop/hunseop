setwd("E:/R")

imdb_dir <- "E:/R/aclImdb/aclImdb"
train_dir <- file.path(imdb_dir, "train")

labels <- c()
texts <- c()


for (label_type in c("neg", "pos")) {
  label <- switch(label_type, neg = 0, pos = 1)
  dir_name <- file.path(train_dir, label_type)
  for (fname in list.files(dir_name, pattern = glob2rx("*.txt"), 
                           full.names = TRUE)) {
    texts <- c(texts, readChar(fname, file.info(fname)$size))
    labels <- c(labels, label)
  }
}


library(keras)

training_samples <- 200      
maxlen <- 100                
validation_samples <- 10000 
max_words <- 10000        

tokenizer <- text_tokenizer(num_words = max_words) %>% 
  fit_text_tokenizer(texts)
sequences <- texts_to_sequences(tokenizer, texts)
head(sequences)

word_index = tokenizer$word_index
cat(length(word_index), "개의 토큰을 찾았습니다.\n")

data <- pad_sequences(sequences, maxlen = maxlen)
labels <- as.array(labels)
cat("data 객체에 저장된 텐서 형식은 :", dim(data), "\n")
cat('labels 객체에 저장된 텐서 형식은 :', dim(labels), "\n")


indices <- sample(1:nrow(data))
training_indices <- indices[1:training_samples]
validation_indices <- indices[(training_samples + 1): 
                                (training_samples + validation_samples)]

x_train <- data[training_indices,]
y_train <- labels[training_indices]
x_val <- data[validation_indices,]
y_val <- labels[validation_indices]

glove_dir = 'E:/R/glove.6B'

lines <- readLines(file.path(glove_dir, "glove.6B.100d.txt"))
head(lines)
embeddings_index <- new.env(hash = TRUE, parent = emptyenv())

for (i in 1:length(lines)) {
  line <- lines[[i]]
  values <- strsplit(line, " ")[[1]]
  word <- values[[1]]
  embeddings_index[[word]] <- as.double(values[-1])
}
View(embeddings_index)

embedding_dim <- 100
embedding_matrix <- array(0, c(max_words, embedding_dim))

for (word in names(word_index)) {
  index <- word_index[[word]]
  if (index < max_words) {
    embedding_vector <- embeddings_index[[word]]
    if (!is.null(embedding_vector))
      embedding_matrix[index+1,] <- embedding_vector
  }
}


model <- keras_model_sequential() %>% 
  layer_embedding(input_dim = max_words, output_dim = embedding_dim, 
                  input_length = maxlen) %>% 
  layer_flatten() %>% 
  layer_dense(units = 32, activation = "relu") %>% 
  layer_dense(units = 1, activation = "sigmoid")

summary(model)


get_layer(model, index = 1) %>% 
  set_weights(list(embedding_matrix)) %>% 
  freeze_weights()

model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy",
  metrics = c("acc")
)

history <- model %>% fit(
  x_train, y_train,
  epochs = 20,
  batch_size = 32,
  validation_data = list(x_val, y_val)
)

getwd()
save_model_weights_hdf5(model, "pre_trained_glove_model.h5")


#사전 훈련망 사용하지 않은 모델 
model <- keras_model_sequential() %>% 
  layer_embedding(input_dim = max_words, output_dim = embedding_dim, 
                  input_length = maxlen) %>% 
  layer_flatten() %>% 
  layer_dense(units = 32, activation = "relu") %>% 
  layer_dense(units = 1, activation = "sigmoid")
model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy",
  metrics = c("acc")
)
history <- model %>% fit(
  x_train, y_train,
  epochs = 20,
  batch_size = 32,
  validation_data = list(x_val, y_val)
)

#최종 평가
test_dir <- file.path(imdb_dir, "test")
labels <- c()
texts <- c()
for (label_type in c("neg", "pos")) {
  label <- switch(label_type, neg = 0, pos = 1)
  dir_name <- file.path(test_dir, label_type)
  for (fname in list.files(dir_name, pattern = glob2rx("*.txt"), 
                           full.names = TRUE)) {
    texts <- c(texts, readChar(fname, file.info(fname)$size))
    labels <- c(labels, label)
  }
}

sequences <- texts_to_sequences(tokenizer, texts)
x_test <- pad_sequences(sequences, maxlen = maxlen)
y_test <- as.array(labels)

model %>% 
  load_model_weights_hdf5("pre_trained_glove_model.h5") %>% 
  evaluate(x_test, y_test, verbose = 0)

