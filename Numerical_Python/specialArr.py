import matplotlib.pyplot as plt
import numpy as np

# Uninitialized array of specific types

a = np.empty(3)
b = np.empty((2, 2))  # All elements essentially zero

# Array with all 0's (Null martix)

c = np.zeros(3)
d = np.zeros((2, 2))

# --- NOTE ---
# np.empty() unlike np.zeros(), deos not set the array values to zero, and may therefore be marginally faster.

# 0's placed in the shape of a given array

e = np.matrix([[1, 2], [3, 4]])
f = np.zeros_like(e)

# Fill the array with a scaler value

g = np.array([1, 2, 3])
g.fill(0)

h = np.arange(1, 10).reshape(3, 3)
h.fill(10)

# Array with all 1's
i = np.ones((3, 3), int)

# Full array (fill the array with a number)

j = np.full((2, 3, 4), 5, int)

# Identity matrix

k = np.identity(3, int)

l = np.eye(4)
l = np.eye(4, k=1)  # On the first upper off-diagonal
l = np.eye(4, k=-1)  # On the first lower off-diagonal

# Diagonal Array

m = np.diag([1, 2, 3, 4])
m = np.diag([1, 2, 3, 4], k=1)  # On the first upper off-diagonal

# fill_diagonal()

np.fill_diagonal(h, 0)
# print(h)

# np.repeat()

n = np.repeat([1, 2, 3], 3)

# Square Wave form

o = np.repeat([0, 1, 0], 100)

plt.plot(o)
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Square Wave")
plt.grid()
# plt.show()

# repeat the entire sequence (np.tile())

p = np.tile([1, 2, 3, 4, 5], 3)
q = np.tile([[1, 2], [3, 4]], 3)  # 2D arrays placed side by side
print(q)
