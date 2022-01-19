import numpy as np


class matrix:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        return self.array + other.array

    def __sub__(self, other):
        return self.array - other.array

    def __mul__(self, other):
        if type(other) == matrix:
            return self.array @ other.array
        else:
            return self.array * other

    def inv(self):
        return np.linalg.inv(self.array)

    def T(self):
        return self.array.T

    def value(self):
        return np.linalg.det(self.array)

    def feature_vector(self):
        return np.linalg.eig(self.array)[0]

    def feature_martix(self):
        return np.linalg.eig(self.array)[1]
    
# m1 = matrix(np.array([1, 23]))
m2 = matrix(np.array(([1, 5],
                      [2, 3])))
m3 = matrix(np.array([[1],
                      [2]]))
ans1, ans2 = np.linalg.eig(m2.array)
print(np.linalg.det(m2.array))
print(ans1)
# print(m1 - m2)
print(m2.feature_vector())
print(m2.T())
