library(keras)

input_tensor<-layer_input(shape =c(64))

output_tensor<-input_tensor %>% 
  layer_dense(units = 32,activation = "relu") %>%
  layer_dense(units = 32,activation = "relu") %>%
  layer_dense(units = 10,activation = "softmax")

model<-keras_model(input_tensor,output_tensor)

summary(model)

model %>% compile(
  optimizer = "rmsprop",
  loss = "categorical_crossentropy",
  metrics = "acc"
)

x_train<-array(runif(1000*64), dim = c(1000,64))
y_train<-array(runif(1000*10), dim = c(1000,10))

model %>% fit(x_train,y_train, epochs = 5, batch_size =128)

model %>% evaluate(x_train,y_train)


####다중 입력 ####

text_vocabulary_size<-10000
ques_vocabulary_size<-10000
answer_vocabulary_size<- 500

text_input<-layer_input(shape = list(NULL),
            dtype = "int32",name = "text")

encoded_text<-text_input %>% 
  layer_embedding(input_dim = text_vocabulary_size + 1 ,
                  output_dim = 32) %>% 
  layer_lstm(units = 32)

question_input<- layer_input(shape = list(NULL),
                             dtype = "int32", name = "question")
encoded_question <- question_input %>% 
  layer_embedding(input_dim = ques_vocabulary_size +1 ,
                  output_dim = 16) %>% 
  layer_lstm(units = 16)

concatenated<-layer_concatenate(list(encoded_text,encoded_question))

answer<-concatenated %>% 
  layer_dense(units = answer_vocabulary_size, activation = "softmax")

model<-keras_model(list(text_input,question_input),answer)

summary(model)

model %>% compile(
  optimizer = "rmsprop",
  loss = "categorical_crossentropy",
  metrics = c("acc")
)

num_samples <- 1000
max_length <-100

text<-random_matrix(1:text_vocabulary_size, num_samples,max_length)
question<-random_matrix(1:ques_vocabulary_size, num_samples,max_length)
answers<- random_matrix(0:1,num_samples, answer_vocabulary_size)

model %>% fit(
  list(text,question),answers,
  epochs =10, batch_size=128
)

model %>% fit(
  list(text = text, question = question),answers,
  epochs =10, batch_size=128
)

#### 다중 출력 모델 ####

library(keras)

vocabulary_size <- 50000  #사용되는 단어 수 
num_income_groups<-10  #10개의 그룹인 소득 수준

posts_input<-layer_input(shape = list(NULL),
            dtype = "int32", name = "posts")

embedded_posts<-posts_input %>% 
  layer_embedding(input_dim = vocabulary_size +1, output_dim = 256)

base_model<-embedded_posts %>% 
  layer_conv_1d(filters = 128, kernel_size = 5, activation = "relu") %>% 
  layer_max_pooling_1d(pool_size = 5) %>%
  layer_conv_1d(filters = 256, kernel_size = 5, activation = "relu") %>%
  layer_conv_1d(filters = 256, kernel_size = 5, activation = "relu") %>%
  layer_max_pooling_1d(pool_size = 5) %>%
  layer_conv_1d(filters = 256, kernel_size = 5, activation = "relu") %>%
  layer_conv_1d(filters = 256, kernel_size = 5, activation = "relu") %>%
  
  layer_global_max_pooling_1d() %>% 
  
  layer_dense(units = 128, activation = "relu")

age_prediction<-base_model %>%
  layer_dense(units = 1,name = "age")

income_prediction<-base_model %>% 
  layer_dense(num_income_groups,activation = "softmax",name = "income")

gender_prediction<- base_model %>%
  layer_dense(units = 1, activation = "sigmoid", name = "gender")

model<-keras_model(
  posts_input,
  list(age_prediction,income_prediction,gender_prediction)
)

summary(model)

model %>% compile(
  optimizer = "rmsprop",
  loss = list(age ="mse", 
              income = "categorical_crossentropy",
              gender = "binary_crossentropy"),
  loss_weights = c(0.25, 1, 10)
)


model %>% fit(
  posts, 
  list(
    age = age_targets,
    income = income_targets,
    gender = gender_targets
  ),
  epochs = 10, batch_size= 64
)

#데이터는 없으며 다중출력을 설명하기 위해 구축된 모델입니다. 실제 학습(x)
