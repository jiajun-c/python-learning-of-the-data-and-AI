# NumPy basic
## 1. create a matrix
```python
arr1 = np.array([1,2,3])
arr2 = np.array([[1], [2], [3]])
```
If you wants to create a array with a gap in a certain 
range, you can use format below
```python
arr = np.arange((1,10,1))
```
you should be careful that whatever ways ypou use to create
a matrix, the format is always `function((number/range))`
If you wants to create the matrix with a certain shape, you
can use the reshape function.
```python
b = np.arange(1, 11, 1).reshape(2, 5)
```
Be careful that the shape a*b must be equal to the
numbers of the matrix

## 2. matrix operation
### the add/sub function
For the + - operation, you can simply use the + - operator
between the matrixs

### the matrix operation
You should use the add instead of the *
```python
c = a@b
```

### the universal operation
If you wants to operator to the every elem in the matrix
you can use the `np.add()`, `np.exp()`, `np.sqrt()`

### the self operation
If you use the += *= ,itself will be changed
If you use the **,the elem will be elem^n
## 3. index, slice, iterate
The index of it is similar to the many dimensions array in
the c++

## 4. reshape the arrays
You can use the reshape function and pass in the len and the wide
,if you worry about making  a WA, you can consider pass in the 
-1 and the numpy will calculate it.

## 5. stack the array together
Sometimes we to merge two matrix together, we have two choices,
one is to merge according to the row, which like
```cpp
1 2   rowmg   1 2   =  1 2 1 2 
1 2           1 1      1 2 1 1  
```

## The copy in the numpy
We must be careful that if you just use the = between two var
,it will not malloc a new space, it is just a reference...
You can judge whether they are the same just by `a is b`
If you wants to use a new space, you can choice to use the copy 
function provide by the numpy, or use the deepcopy method from
the copy library
