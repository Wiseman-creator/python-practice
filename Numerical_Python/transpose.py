import numpy as np

M = np.array([[1, 2, 3], [4, 5, 6]])

print(np.transpose(M))

print(np.fliplr(M))
print(np.flipud(M))

# Rotating (Rotate by 90 deg in the plane specified by specified axes)

print(np.rot90(M, axes=(0, 1)))
print(np.rot90(M, axes=(1, 0)))