# The lambda function
The format for the function is <funciton name> = lambda <par>... : operation
## 1. pass one par
```python
# the one with the single par
Two = lambda x: x * 2
```

## 2. pass many pars
It is almost same with the 1
```python
sub = lambda x, y: x * y
```

## 3. use loop 
The temp var that you use in the loop can be ignored, when you pass in the var 
you one need to pass in other var
```python
fs = [lambda x,y = y: x + y for y in range(11)]
for f in fs:
    print(f(2))
```