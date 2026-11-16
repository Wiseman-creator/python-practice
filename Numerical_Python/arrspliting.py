import numpy as np

x = np.array([2, 3, 4, 5])
x1 = np.split(x, 4)
x2 = np.split(x, 2)

# print(x2)

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

a0 = np.split(A, 3)
# print(a0)
a1 = np.split(A, 4, 1)
# print(a1)

a_v = np.vsplit(A, 3)
a_h = np.hsplit(A, 4)

print(a_v)
print(a_h)

# --- NOTE --- 
# Axis reference is very important for any NumPy method applying to higher dimensions arrays.
# However we do not require axis reference when we use the methods, vspilt() & hspilt()