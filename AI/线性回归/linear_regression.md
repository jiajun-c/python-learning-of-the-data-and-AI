# 单变量的线性回归

## some basic charachter

$m$ means the number of the examples

$x$ means the input

$y$ means the output

We can use the equation $y = \theta_0 + \theta_1 x$ to show the relationship

## the cost function

We can use the function $ J(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^m(h_{\theta}(x^i) - y^i)^2$ to respent the cost



## the use of the cost function

The goal to minimize the $J(\theta_0, \theta_1)$

![Screen Shot 2022-01-17 at 11.47.44 PM](/Users/chengjiajun/Desktop/code/img/Screen Shot 2022-01-17 at 11.47.44 PM.png)

We can draw the picture of the $J(\theta_1)$ by change the $\theta_1$ 

![Screen Shot 2022-01-18 at 8.33.09 AM](/Users/chengjiajun/Desktop/code/img/Screen Shot 2022-01-18 at 8.33.09 AM.png)

## the gradient descent for minimizing the cost function

We keep change the $\theta_0 ,\theta_1$ To get the minimize cost function

 $ \theta_j :=\theta_j -\alpha\frac{\partial J(\theta_0,\theta_1)}{\partial\theta_j}(j = 0, 1) $

$temp0 := \theta_0 - \alpha\frac{\partial J(\theta_0, \theta_1)}{\partial\theta_0}$

$temp1:= \theta_1 - \alpha\frac{\partial J(\theta_0,\theta_1)}{\partial\theta}$

$\theta_0:= temp0$

$\theta_1 :=temp1$

the $\alpha$ is the learning rate of this algorithm a

It is similar to the climb mountain algorithm, every time we change the $\theta_1, \theta_0$ 

If the cost function only have the $\theta_1$ , it will update until it get the point that the derivative is the 0



![Screen Shot 2022-01-18 at 9.04.07 AM](/Users/chengjiajun/Desktop/code/img/Screen Shot 2022-01-18 at 9.04.07 AM.png)


## the example
we get the data from the kaggle, and it is stored in the `线性回归/training_data`
```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
# import needed
train = pd.read_csv("./training_data/train.csv")
test = pd.read_csv("./training_data/test.csv")
train = train.dropna()
test = test.dropna()
# 使用dropna方法去删除我们数据中的空格行
X_train = np.array(train.iloc[:, :-1].values)
y_train = np.array(train.iloc[:, 1].values)
X_test = np.array(test.iloc[:, :-1].values)
y_test = np.array(test.iloc[:, 1].values)
# smodel = LinearRegression(fit_intercept=True, normalize=True, copy_X=True, n_jobs=-1)
# this model is a old style, and it will get the warning
model = make_pipeline(StandardScaler(with_mean=False), LinearRegression())
# 对我们的数据进行处理,得到合适的数据
model.fit(X_train, y_train)
# 使用我们的训练数据进行训练
y_pred = model.predict(X_test)
accuracy = model.score(X_test, y_test)
# 使用测试数据得到我们的模型的准确性
plt.plot(X_train, model.predict(X_train), color='green')
plt.savefig("./output_img/out1.png")
print(accuracy)
```

[参考](https://www.kaggle.com/kareem3egm/learn-machine-learning-faster-1)
## some limitation of this algorithm, you may come to a local best soluation

It is called the batch gradient descent alghorithm.

## Multple features(varibles) 

![Screen Shot 2022-01-19 at 11.39.22 AM](/Users/chengjiajun/Desktop/code/img/Screen Shot 2022-01-19 at 11.39.22 AM.png)

one training example consist of the [x1... y]

Hypothesis: $h_{\theta}(x) = \theta^Tx$

Parameters: $\theta_1...\theta_n$

Cost_function: $J(\theta_0,\theta_1..\theta_n) = \frac{1}{2m}\sum_{i=1}^m(h_{\theta}(x^i) - y^i)x^i$

Gradient descent:

​	Repeat {

​		$\theta_j := \theta_j - \alpha\frac{\partial J}{\partial\theta_j}$

}

be remind. that the $x_0$ is the 1

### the fearure scaling

make sure feature are on a similar scale

<img src="/Users/chengjiajun/Library/Application Support/typora-user-images/Screen Shot 2022-01-19 at 1.51.08 PM.png" alt="Screen Shot 2022-01-19 at 1.51.08 PM" style="zoom: 67%;" />

Now goes on the $\theta_2$ it will be slow

We can sub the x1 with the 2000 and sub the x2 with the 5

So the target of this it to make every varible are in the range (-1, 1)

### the mean normalization

We can replace the $x_i$ with the $x_i - u_i$ to make sure that the average of the varible have the average of the zero

### the choose of the $\alpha$

In some situation, we can see with the $\alpha$ is too big, if the tendency is like belw, we should try to use a small $\alpha$

![Screen Shot 2022-01-19 at 2.18.56 PM](/Users/chengjiajun/Library/Application Support/typora-user-images/Screen Shot 2022-01-19 at 2.18.56 PM.png)



### the feature and the quantic regression

We can define the new feature to solve our problem. 

When use create the new feature, it is important to use the mean normalization

We can use the $\sqrt{x}, x^2 ...$

# the normal equation method

![Screen Shot 2022-01-19 at 2.42.57 PM](/Users/chengjiajun/Desktop/code/img/Screen Shot 2022-01-19 at 2.42.57 PM.png)

You can find the $\theta$ simply by solve the equation

The ans above may look like .....,but you can verify it

## the conclusion

When the n is large, the gradient works well, but it may need may times of the iterator

because the normal opmtize for the equation is much slower.



ps: in some times, the equation may be invertible. 

