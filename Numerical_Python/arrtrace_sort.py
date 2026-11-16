import numpy as np

# Trace of a 2D array or mateix is the sum of its diagonal elements.
# We give the offset reference to pick some dagonal(Main diagonal or any diagonal on the up and down directions)

A = np.array([[-1, -4, -2, 6], [-9, 2, 6, 0], [-6, -4, 0, 2], [-1, 2, 6, 1]])

traceA = np.trace(A)  # Sum of the diagonal elements of main diagonal
print(traceA)
t1 = np.trace(A, 1)  # Sum of the 1st upper off diagonal
print(t1)
t1 = np.trace(A, -1)  # Sum of the 1st lower off diagonal
print(t1)

# Sorting of elements

x = np.array([-1, -4, -2, 6, -9, 2, 6, 0, -6, -4, 0, 2, -1, 2, 6, 1])

print(np.sort(x))  # Ascending order
print(np.sort(x)[::-1])  # Decending order

arr = np.array([[2, 4, 3, 5], [1, 6, 4, 3], [2, 5, 7, 4], [3, 1, 6, 8]])
# print(arr)
# print(np.sort(arr, 0))
# print(np.sort(arr, 1))

l = np.array([10, 6, 12])
ind = np.argsort(l)  # Return position indices
print(ind)
print(l[ind])  # Sorted through index positions

c = np.array([[1, 5, 20], [5, 7, 64], [3, 9, 97], [2, 4, 38], [4, 6, 90]])

c0 = c[:, 0]
c1 = c[:, 1]

print(c[np.argsort(c0)])  # Sorting rows through 1st coloumn
print(c[np.argsort(c1)])  # Sorting rows through 2st coloumn
