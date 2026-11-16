import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])
# print(a)
# np.put(a,2,0)
# print(a)    # The original array is changed

A = np.insert(a,2,0)
print(A)    # It returns a new array

# NOTE --- The difference between the two method is that np.put() returns nothing.It alters the array itself.
# But inserting through np.insert() returns a new array while keeping the old array unchanged.

b = np.array([[1, 2],[3, 4]])
b1 = np.insert(b, 1, [0, 0], axis=0)     # Along the row
print(b1)

b2 = np.insert(b, 1, [0, 0], axis=1)   # along the coloumn
print(b2)

z = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

z_rdel = np.delete(z,1,axis=0)
print(z_rdel)

z_cdel = np.delete(z,1,axis=1)
print(z_cdel)