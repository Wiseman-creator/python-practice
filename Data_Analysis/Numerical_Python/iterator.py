import numpy as np

# Numpy are iterable objects.

x = np.array([1, 2, 3, 4])

A = np.array([[1, 2, 3], [4, 5, 6]])

for i in x:
    print(i,end=' ')    # 1 2 3 4 

print()

for i in A:
    print(i,end=' ')    # [1 2 3] [4 5 6] 

# For iterating over 2D array with order we use np.nditer(),
# which iterates over an array to get the entries in a sequence.
# order = 'F' --- iterating in FORTRAN or by coloumnwise.
# order = 'C' --- iterating in C or by rowwise.

print()

for i in np.nditer(A, order='C'):
    print(i,end=' ')   

print()

for i in np.nditer(A, order='F'):
    print(i,end=' ')   

print()
