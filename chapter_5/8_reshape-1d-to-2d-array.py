from numpy import array


data = array([11, 22, 33, 44, 55])
print(data.shape)
print(data)

# Convierte un array de una dimension en una matriz de 2 dimensiones [1, X] => [X, 1]
data = data.reshape((data.shape[0], 1))
print(data.shape)
print(data)
