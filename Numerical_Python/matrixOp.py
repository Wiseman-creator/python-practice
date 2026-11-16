import numpy as np

a = np.matrix([[1, 2, 3], [3, 4, 5]])

b = np.matrix([[1, 2], [3, 4], [5, 6]])

s = np.matrix([[1, 2], [3, 4]])

t = np.matrix([[5, 6], [7, 8]])

# print(type(a))
# print(a)

# print(a * b)
# print(a.T)
# print(a.T + b)

# Complex Matrix

c = np.matrix([[1 + 2j, 3 + 4j], [5 + 6j, 7 + 8j]])

print(c.T)  # Transpose
print(c.H)  # Conjugate
