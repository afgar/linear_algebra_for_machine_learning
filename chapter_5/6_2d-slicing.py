from numpy import array

data = array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]])

X, y = data[:, :-1], data[:, -1]

print(X)  # Todas las filas y todas las columnas menos la ultima
print(y)  # Todas las filas y solo la última columna

split = 2
train, test = data[:split, :], data[split:, :]  # Divide el dataset en la parte que se entrena y la que se prueba
print(train)
print(test)
