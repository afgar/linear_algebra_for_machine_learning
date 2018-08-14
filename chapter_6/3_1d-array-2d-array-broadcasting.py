# broadcast one-dimensional array to two-dimensional array
from numpy import array

A = array([
    [1, 2, 3],
    [1, 2, 3]])
print(A)

b = array([1, 2, 3])
print(b)

C = A + b
print(C)
