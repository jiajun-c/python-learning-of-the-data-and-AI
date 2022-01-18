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



## some limitation of this algorithm, you may come to a local best soluation

It is called the batch gradient descent alghorithm.



