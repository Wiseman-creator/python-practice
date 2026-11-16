import numpy as np

a = np.array([[4, 3], [5, 6]])

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

det_a = np.linalg.det(a)

# print(type(det_a))
# print(round(det_a))

det_A = np.linalg.det(A)

# print(type(det_A))
# print(round(det_A))

# Adjoint of a matrix
# def adjugate(A):
#     n = A.shape[0]
#     C = np.zeros(A.shape, dtype=float)

#     for i in range(n):
#         for j in range(n):
#             M = np.delete(A, i, axis=0)
#             M = np.delete(M, j, axis=1)

#             C[i, j] = (-1)**(i+j) * np.linalg.det(M)

#     return C.T

# print(adjugate(a))

# Rank of a matrix

rank = np.linalg.matrix_rank(A)
# print(rank)

# Inverse of a matrix

inv = np.linalg.inv(a)
# print(inv)

m = np.array([[1, 2, -1], [2, 1, 4], [3, 3, 4]])
n = np.array([1, 2, 1])

m_inv = np.linalg.inv(m)
X = np.dot(m_inv, n)
# print(X)
# print(np.linalg.solve(m, n))

