from numpy import array

A = array([
    [1, 2, 3],
    [1, 2, 3]])
print(A)

b = 2
print(b)

# Internamente es como si crease una matriz de igual que A pero con un 2 en cada celda
c = A + b
print(c)
