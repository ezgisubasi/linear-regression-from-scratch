# linear-regression-from-scratch

This program performs linear regression with one variable using a stochastic gradient descent algorithm which fits a line to a given dataset. The equation y = mx + n is used to find the best fitting linear function, and m and n parameters in this function are found by gradient descent. When linear regression is with one variable, a method called analytical solution can be applied instead of gradient descent. In this program, accuracy is measured by comparing the results of stochastic gradient descent and analytical solution.


# Stochastic Gradient Descent

The gradient descent algorithm aims to find the lowest point on the surface by taking the slopes of the points. Rather than gradient descent, random data is taken at each step in the stochastic gradient descent algorithm, and the descent proceeds to find the best lowest point.

<p align="center"> 
  <img width="400" alt="sgd2" src="https://user-images.githubusercontent.com/52889449/121677065-129fed80-cabe-11eb-84c8-d80fac6dbc21.png"> 
</p>

In each step, the slope of the next point is calculated, this process is continued until the result found is close to the given threshold. Also, the algorithm follows the formula for new parameter by new = old - step size so that the algorithm can progress. 

<p align="center"> 
  <img width="400" alt="sgd" src="https://user-images.githubusercontent.com/52889449/121677051-0d42a300-cabe-11eb-885f-a61f87828551.png"> 
</p>

While calculating the next step for each point, the formula step size = gradient * learning rate is applied. Thus, the size of the step can be controlled according to the learning rate and it prevents the problems caused by too large or too small steps as in the image.

<p align="center"> 
<img width="1376" alt="Ekran Resmi 2021-06-11 14 31 14" src="https://user-images.githubusercontent.com/52889449/121680017-b63ecd00-cac1-11eb-9f62-78217e682c1c.png">
</p>

The lowest point I mentioned is called the global minimum and other lower points are called local minimum as you can see in the figure. It may not always be possible to find the lowest point (global minimum) in gradient descent algorithms.

<p align="center"> 
<img width="400" alt="Ekran Resmi 2021-06-11 14 23 22" src="https://user-images.githubusercontent.com/52889449/121679075-a1156e80-cac0-11eb-9911-3951aef16a1f.png">
</p>


# Outputs of given dataset with different Learning Rates

Learning Rate = 0.001

<p align="center">
 <img width="400" alt="Ekran Resmi 2021-06-11 14 00 15" src="https://user-images.githubusercontent.com/52889449/121676550-6fe76f00-cabd-11eb-8955-378c10e2e1dd.png"> 
 <img width="400" alt="Ekran Resmi 2021-06-11 14 00 24" src="https://user-images.githubusercontent.com/52889449/121676559-71b13280-cabd-11eb-9851-0bd0ec7b6c9b.png"> 
</p>

Learning Rate = 0.01 

<p align="center">
<img width="400" alt="Ekran Resmi 2021-06-11 14 00 31" src="https://user-images.githubusercontent.com/52889449/121676604-7c6bc780-cabd-11eb-8272-7f10531f17f6.png">
<img width="400" alt="Ekran Resmi 2021-06-11 14 00 42" src="https://user-images.githubusercontent.com/52889449/121676608-7d9cf480-cabd-11eb-8ffa-3bfd96a8206d.png">
</p>
