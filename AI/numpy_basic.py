import numpy as np
import copy
from numpy import newaxis as nx
import matplotlib as mb

vector_row = np.array([1, 2, 3])
vector_col = np.array([[1], [2], [3]])
print("{}\n{}".format(vector_row, vector_col))
# reshape can control the shape of the matrix, and the range is the control by the np.arange
arr = np.arange(15).reshape(3, 5)
print("the array is {}, \n and the size is the {}\n The dim is {}".format(arr, arr.size, arr.ndim))

# create a array
print(np.zeros((3, 4), dtype=np.int64))

print(np.ones((3, 4), dtype=np.int64))

# np.range means the start end the gap
print(np.arange(1, 10, 1))

# the np.arange can be combined with the reshape
b = np.arange(1, 11, 1).reshape(2, 5)
print(b)

# the basic operation

sub1 = np.array([1, 2, 3])
sub2 = np.array([2, 2, 3])
print(sub2 - sub1)

a1 = np.array([[1, 2],
               [2, 2]])
a2 = np.array([[1, 0],
               [1, 0]])

# you should be careful that the * between the np arrary is not the sub of the matrix, if you wants to sub  between be
# matrix , you should use the @ instead
print(a1 * a2)

print(a1 @ a2)

a1 *= 3
print(a1)

# the universal function
# the ufunction means it only works on the elem of the matrix

a1 = np.exp(a1)
print(a1)

# the similar function like
# np.add()
# np.sqrt()

# index, sile and iterating

a1 += 3
print(a1)

print(a2)
a2 += 1
print(a2)

a2 = a2 ** 3
print(a2)

print(a2[0])

a3 = np.arange(1, 10, 1)
a3 = a3.reshape(3, 3)
print(a3)
a3 = a3.reshape(9, -1)
print(a3)
a3.ravel()

b1 = np.zeros((2, 2))
b2 = np.ones((2, 2))
b3 = np.row_stack((b1, b2))
b3 = np.column_stack
b4 = np.vstack((b1, b2))
print(b4)
print(b3)
# the row_stack merge the b1 and the b2 according to the row
# the cloumn_stack merge in the column

b5 = np.zeros((2,2))
b6 = b5
b6[1][1] = 6
print(b5)

b6 = copy.deepcopy(b5)
print(b6 is b5)