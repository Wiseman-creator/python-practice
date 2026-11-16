import numpy as np

a = np.array([[4, 1], [2, 3]])

print("Given matrix:\n", a)
# Square matrix check ---
print("Shape of matrix:", a.shape)

if a.shape[0] == a.shape[1]:
    print("It's a square matrix.")
else:
    print("It's not  a square matrix.")
    raise ValueError

# Charecteristic polynomial ---

coeff = np.poly(a)

print("Charecteristic polynomial coeffecients of the matrix:", coeff)

# Eigen value & Eigen vector ---

values, vectors = np.linalg.eig(a)

print("Eigen value:", values)
print("Eigen vectors:\n", vectors)

print("Trace:", np.trace(a))
print("Sum of eigenvalues:", np.sum(values))

print("Determinant:", np.linalg.det(a))
print("Product of eigenvalues:", np.prod(values))
