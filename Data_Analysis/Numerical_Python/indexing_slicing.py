import numpy as np

arr = np.array([1, 4, 7, 10, 13, 16, 19])

# print(arr[0])
# print(arr[-1])
# print(arr[int(len(arr)/2)])

arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr3D = np.array(
    [
        [[1, 2, 9], [3, 4, 9], [1, 1, 1]],
        [[4, 5, 9], [5, 6, 9], [1, 1, 1]],
        [[6, 7, 9], [7, 8, 9], [1, 1, 1]],
    ]
)

# print(arr3D[1][1][1])

# Slicing of Arrays

x = np.array([1, 4, 7, 10, 13, 16, 19])

x1 = x[1:7:2]
# print(x1)

x_rev = x[::-1]
# print(x_rev)

y = np.array(
    [
        [[1, 2, 9], [3, 4, 9], [1, 1, 1]],
        [[4, 5, 9], [5, 6, 9], [1, 1, 1]],
        [[6, 7, 9], [7, 8, 9], [1, 1, 1]],
    ]
)

# print(y[::-1,::-1]) # Row and coloumn reverse

# Slice by conditional statement

z = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(z[z > 3])  # it returns flatten arrays
