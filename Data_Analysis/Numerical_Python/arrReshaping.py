import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])

# print(a.shape)
b = a.reshape(2,3)
c = a.reshape(3,2)

# print(c)

# print(np.size(a))   # 6

a.resize(2,3)   # Resize changes the original array 
print(a)

# NOTE --- The reshape() function returns a new array with a modified shape whereas the resize() modifies the array itself.

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(x.flatten())
print(x.flatten(order='F'))

print(x.ravel())

# NOTE --- In NumPy, both flatten() and ravel() convert a multidimensional array into a one-dimensional array.

# The main difference is how they handle memory.
# - flatten() always returns a copy.
# - ravel() returns a view whenever possible, otherwise it creates a copy.ravel() returned a view sharing the original array's memory.