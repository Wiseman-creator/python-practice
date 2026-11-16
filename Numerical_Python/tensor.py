import numpy as np

T = np.arange(1, 19).reshape(2, 3, 3)
print(T.shape)

# The element wise product between two tensor of the same dimension will result in a new tensor with same dimension.
# Such product is called Hadamard Product

# Tensor product is quite different than the Hadamard product. 
# If two tensors A & B have dimensions p & q then the resulting tensor product will have dimension p+q

A = np.array([1,2,3])   # tensor of rank 1
B = np.array([4,5])     # tensor of rank 1

C = np.tensordot(A, B, 0)      # tensor of rank 2
# print(C.shape)
# print(C)

a = np.array([[1,2,3],[4,5,6]]) 
b = np.array([[1,0,-1],
              [1,2,1]]) 

c = np.tensordot(a, b, axes=0)
print(c.shape)

c = np.tensordot(a, b.T, axes=1)
print(c.shape)