import numpy as np

x = np.array([[2, 3, 4], [5, 6, 7]])
y = np.array([[12, 13, 14], [25, 26, 27]])
z = np.array([["a", "b", "c"], ["d", "e", "f"]])

# stack along axis = 0

w0 = np.stack((x, y, z), axis=0)
print(w0)
print(w0.shape)
print()

# stack along axis = 1(horizontal direction)

w1 = np.stack((x, y, z), axis=1)
print(w1)
print(w1.shape)
print()

# stack along axis =2

w2 = np.stack((x, y, z), axis=2)
print(w2)
print(w2.shape)
print()

# --- NOTE ---
# Stacking of 2D arrays returns 3D arrays in all cases,only the order changes.

# Vertical Stack
# It is similar to concatenation

w_v = np.vstack((x, y, z))
print(w_v)
print(w_v.shape)
print()

# Horizontal Stack

w_h = np.hstack((x, y, z))
print(w_h)
print(w_h.shape)
print()

# Depthwise stacking
# adds a new axis and stack
w_d = np.dstack((x, y, z))
print(w_d)
print(w_d.shape)
print()
