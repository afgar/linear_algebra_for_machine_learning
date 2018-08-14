from numpy import array

data = array([11, 22, 33, 44, 55])
print(data.shape)

data = [[11, 22],
        [33, 44],
        [55, 66]]

data = array(data)
print(data.shape)

print('Rows: %d ' % data.shape[0])
print('Cols: %d ' % data.shape[1])
