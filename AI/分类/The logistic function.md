# The logistic function

We have a signmod function that looks like the 

$h_{\theta}(x) = \frac{1}{1+e^{-\theta^Tx}}$

$h_{\theta}(x) = P(y=1|x;\theta)$ it means under the x. and the $\theta$ the possibility for the y to be the 1

We always make the $g(x) = \frac{1}{1+e^{-x}}$, and the plot is like the below



<img src="/Users/chengjiajun/Library/Application Support/typora-user-images/Screen Shot 2022-01-22 at 2.35.48 PM.png" alt="Screen Shot 2022-01-22 at 2.35.48 PM" style="zoom: 67%;" />

## The decision boundary

​	We can simply makes the 0.5 a boundary, so in this mode when the $\theta^Tx$ >= 0, the output is the 1, others the output is the 0

![Screen Shot 2022-01-22 at 3.00.50 PM](/Users/chengjiajun/Desktop/code/python_learning/AI/分类/img/Screen Shot 2022-01-22 at 3.00.50 PM.png)

In this situation, we can find that the boudary is x1 + x2 + 3 = 0

If the data is a non-linear decision boundary, we can using the polynomial.

If we using the higher polynomial, we can get the more complex shape

## How to fit the $\theta$

$J(\theta) = \frac{1}{m}\sum_{i=1}^m cost(h_{\theta}(x^{i})-y_i) $

$cost(h_\theta(x),y)=\frac{1}{2}(h_{\theta}(x)-y)^2$

But the cost function for the is not the convex, and we need  a new one



<img src="/Users/chengjiajun/Library/Application Support/typora-user-images/Screen Shot 2022-01-22 at 3.15.57 PM.png" alt="Screen Shot 2022-01-22 at 3.15.57 PM" style="zoom:67%;" />



It can be simplify to the $Cost(h_\theta(x),y)=-y\log(h_{\theta}(x))-(1-y)\log(1-h_{\theta}(x))$

because the y can only be the 1/0

<img src="/Users/chengjiajun/Desktop/code/python_learning/AI/分类/img/Screen Shot 2022-01-22 at 3.25.10 PM.png" alt="Screen Shot 2022-01-22 at 3.25.10 PM" style="zoom:80%;" />

We can using the gradient descnet to find the $\theta$

## mult-class classfication

##  ![Screen Shot 2022-01-22 at 3.40.26 PM](/Users/chengjiajun/Desktop/code/python_learning/AI/分类/img/Screen Shot 2022-01-22 at 3.40.26 PM.png)

We can make many classfier, that every time, it dived a type from the sample

and when we need to find the belonging, we just need to choice the one with be biggest posibility

