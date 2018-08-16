# matrix Hadamard product C = A ◦ B
from numpy import array

# define first matrix
A = array([
    [1, 2, 3],
    [4, 5, 6]])
print(A)

# define second matrix
B = array([
    [1, 2, 3],
    [4, 5, 6]])
print(B)

# multiply matrices
C = A * B
print(C)
