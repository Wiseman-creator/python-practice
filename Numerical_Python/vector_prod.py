import numpy as np

u = np.array([1, 2, 3])
v = np.array([-1, 0, 1])

dot = np.vdot(u, v)
cross = np.cross(u, v)

print(dot)
print(cross)

# Volume Calculation of parallelopiped

A = np.array([2, -3, 0])
B = np.array([1, 1, -1])
C = np.array([3, 0, -1])

vol = np.inner(A, np.cross(B, C))

print("Volume of the parallelopiped:", vol, "unit")

# For multi-dimensional arrays

s = np.array([[1, 2], [3, 4]])
t = np.array([[5, 6], [7, 8]])

# Inner product between 2D arrays
print(np.inner(s, t))
# this is useful for getting vector result like A X B
# Vector dot product for multidimensional arrays
print(np.vdot(s, t))
# this is useful for getting vector result like A . B

print(s+t)      # Matrix like addition
print(np.dot(s,t))   # Matrix like product
print(s@t)
# np.dot() between two vectors gives same result as np.inner()