# The basic of the list operation
## 1.create a list
```python
a = [1,2,3,4]
```

## 2. add or remove the elem
The remove function will remove the elem that you pass in, if you pass in the 1
the 1 will not exist in you list
```python
a.append(1)
a.remove(1)
```
## 3.sort the list
You can use the sort function
```python
a.sort(<list>,<cmp_function>,<reversed>)
```
The cmp_function is same to the function you use in the c/cpp
The elem that with the smaller value in the function wil be placed 
in the front of the list
,the reserve function wil decide that whether the list will be reserved

## 4. cut the list
In the cut of the list you will need to pass two par, the l and the r, and 
it will cut the $a[l] \to a[r-1]$

```python
b = a[1:3]
```
