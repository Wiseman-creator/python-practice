import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

print(x + y)  # [ 6  8 10 12]
print(x - y)  # [-4 -4 -4 -4]
print(x * y)  # [ 5 12 21 32]
print(x / y)  # [0.2 0.33333333 0.42857143 0.5]
print(x // y)  # [0 0 0 0]
print(x**y)  # [1 64  2187 65536]

print(x**2 + y**3)  # [126 220 352 528]

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[4, 5, 6], [1, 1, 1]])

C = np.add(A, B)  # Using NumPy method
print(C)

print(A + [[1], [10]])  # addition in coloumn
print(A + [10, 10, 10])  # addition in row
