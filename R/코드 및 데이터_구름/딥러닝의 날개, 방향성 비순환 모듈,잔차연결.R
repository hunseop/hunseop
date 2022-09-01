####방향성 비순환 모듈 ####

library(keras)

input_tensor <- layer_input(shape = c(64,32,32),name = "INPUT_TENSOR")

branch_a<-input_tensor %>%
layer_conv_2d(filters = 128, kernel_size = 1,
activation = "relu",strides = 2,name = "branch_a")

summary(branch_a)

branch_b <-input_tensor %>%
layer_conv_2d(filters = 128, kernel_size = 1,
activation = "relu") %>%
layer_conv_2d(filters = 128, kernel_size = 1,
activation = "relu",strides = 2, name = "branch_b")

summary(branch_b)

branch_c <- input_tensor %>%
layer_average_pooling_2d(pool_size = 1, strides = 2) %>%
layer_conv_2d(filters = 128, kernel_size = 1,
activation = "relu",name = "branch_c")

summary(branch_c)

branch_d <- input_tensor %>%
layer_conv_2d(filters = 128, kernel_size = 1,
activation = "relu") %>%
layer_conv_2d(filters = 128, kernel_size = 1,
activation = "relu") %>%
layer_conv_2d(filters = 128, kernel_size = 1,
activation = "relu",strides = 2,name = "branch_d")

summary(branch_d)

concatenate<-layer_concatenate(list(
branch_a,branch_b,branch_c,branch_d))

branch_set <- layer_dense(concatenate, 
                          units = 1, 
                          activation = "sigmoid")

model <- keras_model(inputs = input_tensor, 
                     outputs = branch_set)

summary(model)


model <- application_inception_v3(include_top = TRUE,
                                  weights = "imagenet",
                                  classes = 1000)



#### 잔차연결 ####

library(keras)

input_tensor<-layer_input(shape =c(28,28,1),name = "INPUT")

output<-input_tensor %>% 
  layer_conv_2d(filters = 32, kernel_size = c(3,3), 
                activation = "relu",padding = "same",name = "layer_1") %>%
  layer_conv_2d(filters = 64, kernel_size = c(3,3), 
                activation = "relu",padding = "same",name = "layer_2") %>%
  layer_max_pooling_2d(pool_size = 2, strides = 2,name = "layer_output")

residual<-input_tensor %>%
  layer_conv_2d(filters = 64, kernel_size = c(2,2), strides = 2,name = "layer_residual")

output<-layer_add(list(output, residual))

model<-keras_model(input_tensor,output)

summary(model)

