import numpy as np

arr1 = np.array([1, 2, 3])

# print(arr.dtype)
# print(arr.itemsize)

# int8        -128 - 127
# int16       -32768 - 32767
# int32, int64
# uint8       0 - 255
# uint16, uint32, uint64
# float16, float32, float64
# complex64, complex128

arr = np.array([2 + 3j, 4 + 5j])

print(arr.dtype)
# print(arr.real)
# print(arr.imag)

a = np.array(["Abc", "101", 99])
print(a.dtype)

# Data type Enforced

x = np.array([10, -2.4, 1], dtype=int)
print(x.dtype)
x = np.array([10, -2.4, 1], dtype=float)
print(x.dtype)
x = np.array([10, -2.4, 1], dtype=complex)
print(x.dtype)

#  we can specify the exact data type like int16 or complex64
# And we can also set the data type using the acronym like
# i1 = int8, i2 = int16, int32 = i3, int64 = i4
# f2 = float16, float32 = f3, float64 = f4

s1 = np.array(["Abc", "101", 99], dtype="S4")
print(s1.dtype)
print(s1)

# Convert to a specific type

a = np.array([2, 4, 6, 8])
b = a.astype("float")
print(a)  # astype() does not change the original array
print(b)

z = np.array([2 + 3j, 4 + 5j, 6 + 7j])
Re_z = z.real  # type: ignore
Im_z = z.imag  # type: ignore
print(z)
print(Re_z)
print(Im_z)
print(z.conj())
