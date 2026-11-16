import numpy as np

A = np.array([[2, 3], [1, 4]])

det_A = np.linalg.det(A)

if not np.isclose(det_A, 0):
    print("Non-Singular Matrix.")
    print("Inverse:")
    print(np.linalg.inv(A))

else:
    print("Singular Matrix.")
