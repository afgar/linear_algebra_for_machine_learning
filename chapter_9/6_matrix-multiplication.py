# matrix dot product C = AB
from numpy import array

# define first matrix
A = array([
    [1, 2],
    [3, 4],
    [5, 6]])
print(A)

# define second matrix
B = array([
    [1, 2],
    [3, 4]])
print(B)

# multiply matrices
C = A.dot(B)
print(C)

# multiply matrices with @ operator
D = A @ B
print(D)

# The number of columns (n) in the first matrix (A) must equal the number of rows (m) in the second matrix (B).
# For example, matrix A has the dimensions m rows and n columns and matrix B has the dimensions n and k. The n columns
# in A and n rows in B are equal. The result is a new matrix with m rows and k columns.
