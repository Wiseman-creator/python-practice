import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])
b = np.array([0, 20, 30, 40, 50, 60])

z = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

z0 = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]])

# print(np.all(a))
# print(np.all(b))

# print(np.all(z))
# print(np.all(z0))
# Test wheteher alll array elements alon a given axis zero or not

# Where statement
# It is often used to search a particular element and to know where does it lie in the array.

x = np.array([1, 4, 7, 10, 13, 16, 19])

# print(np.where( x == 10 ))
# print(np.where( z == 6 ))

r = np.random.randint(1,100,size= (3,3,3))
# print(r[r>50])
R = np.where(r<50, 0, r)
# print(r)
# print(R)

# Unique Elements

m = np.random.randint(1, 7, 10000)
print(np.unique(m))