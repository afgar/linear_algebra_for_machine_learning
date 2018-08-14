from numpy import array

data = array([[11, 22],
              [33, 44],
              [55, 66]])

print(data.shape)
print(data)

# Reorganiza la matriz y la convierte en un array de 3 dimensiones
data = data.reshape((data.shape[0], data.shape[1], 1))
print(data.shape)
print(data)
