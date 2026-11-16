import numpy as np

# Swap is to interchange the position of two elements

a = np.array([10, 20, 30, 40, 50, 60])
a[[1,2]] = a[[2,1]]
print(a)    # [10 30 20 40 50 60]

z = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

z[[1,2]] = z[[2,1]]
print(z)    # Interchange of row 2 & 3

z[:, [1,2]] = z[:, [2,1]]
print(z)    # # Interchange of coloumn 2 & 3