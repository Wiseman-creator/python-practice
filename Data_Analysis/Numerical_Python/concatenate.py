import numpy as np

x = np.array([1, 3, 5, 7, 9])
y = np.array([2, 4, 6])

new_x = np.append(x, y)
# print(new_x)

z = np.array([[1, 3], [5, 7]])
w = np.array([[2, 3], [0, 1]])
new_z = np.append(z, [[9, 9]], axis=0)
# print(new_z)

new_z1 = np.append(z, [[9], [9]], axis=1)
# print(new_z1)

xy = np.concatenate((x, y))
# print(xy)

zw = np.concatenate((z, w), axis=1)
print(zw)
