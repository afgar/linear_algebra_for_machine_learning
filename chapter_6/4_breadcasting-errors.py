from numpy import array

# El briadcasting solo se permite si el ultimo elemento de shape es 1 o igual entre matrices y vectores
# Ej:
# Esto:
# A.shape = (2 x 3)
# b.shape = (3)
#
# es igual a esto:
# A.shape = (2 x 3)
# b.shape = (1 x 3)
#
# Esto falla
# A.shape = (2 x 3)
# b.shape = (1 x 2)

A = array([
    [1, 2, 3],
    [1, 2, 3]])

print(A.shape)

b = array([1, 2])
print(b.shape)

C = A + b
print(C)
