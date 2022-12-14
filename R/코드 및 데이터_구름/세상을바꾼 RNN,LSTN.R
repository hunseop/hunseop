#### RNN layer ####

library(keras)

layer_simple_rnn(units = 32)

model_1<-keras_model_sequential() %>% 
  layer_embedding(input_dim = 10000, output_dim = 32) %>% 
  layer_simple_rnn(units = 32)

summary(model)


model_2<-keras_model_sequential() %>% 
  layer_embedding(input_dim = 10000,output_dim = 32) %>% 
  layer_simple_rnn(units = 32,return_sequences = TRUE)

summary(model_2)

model<-keras_model_sequential() %>% 
  layer_embedding(input_dim = 10000,output_dim = 32) %>% 
  layer_simple_rnn(units = 32,return_sequences = TRUE) %>% 
  layer_simple_rnn(units = 32,return_sequences = TRUE) %>% 
  layer_simple_rnn(units = 32,return_sequences = TRUE) %>% 
  layer_simple_rnn(units = 32,return_sequences = TRUE) %>% 
  layer_simple_rnn(units = 32) 

summary(model)


max_features<-10000 #특징들로 간주할 단어 수

imdb<-dataset_imdb(num_words = max_features)
c(c(input_train, y_train), c(input_test,y_test))%<-% imdb

maxlen<-500 #문장당 500단어까지만 사용
input_train<-pad_sequences(input_train,maxlen = maxlen)
input_test<-pad_sequences(input_test,maxlen = maxlen)

model<-keras_model_sequential() %>% 
  layer_embedding(input_dim = max_features, output_dim = 32) %>% 
  layer_simple_rnn(units = 32,return_sequences = TRUE) %>% 
  layer_simple_rnn(units = 32) %>% 
  layer_dense(units = 1, activation = "sigmoid")

summary(model)

model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy",
  metrics = c("acc")
)

history<-model %>% fit(
  input_train,y_train,
  epochs = 10,
  batch_size =128,
  validation_split = 0.2
)

#### LSTM layer ####

library(keras)

model <- keras_model_sequential() %>% 
  layer_embedding(input_dim = max_features, output_dim = 32) %>% 
  layer_lstm(units = 32) %>% 
  layer_dense(units = 1, activation = "sigmoid")

model %>% compile(
  optimizer = "rmsprop", 
  loss = "binary_crossentropy", 
  metrics = c("acc")
)

history <- model %>% fit(
  input_train, y_train,
  epochs = 10,
  batch_size = 128,
  validation_split = 0.2
)









