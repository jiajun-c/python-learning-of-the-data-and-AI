from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
import tensorflow
# 加载数据集
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 数据集预处理
X_train = X_train.reshape(-1, 1, 28, 28)
X_test = X_test.reshape(-1, 1, 28, 28)

# 将label变为向量
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)


# 构建神经网络
model = Sequential()

# 卷积层一
model.add(Conv2D(32, kernel_size = (5, 5), strides = (1, 1), padding = 'same', activation = 'relu', input_shape = (1, 28, 28)))

# 池化层一
model.add(MaxPooling2D(pool_size = (2, 2), strides = (1, 1), padding = 'same'))

# 卷积层二
model.add(Conv2D(64, kernel_size = (5, 5), strides = (1, 1), padding = 'same', activation = 'relu'))

# 池化层二
model.add(MaxPooling2D(pool_size = (2, 2), strides = (1, 1), padding = 'same'))

# 全连接层一
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))

# 全连接层二
model.add(Dense(10))
model.add(Activation('softmax'))

# 选择并定义优化求解方法
adam = Adam(lr = 1e-4)

# 选择损失函数、求解方法、度量方法
model.compile(optimizer = adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])

# 训练模型
model.fit(X_train, y_train, epochs = 2, batch_size = 32)

# 评估模型
loss, accuracy = model.evaluate(X_test, y_test)


print ("")
print ('loss: ', loss)
print ('accuracy: ', accuracy)