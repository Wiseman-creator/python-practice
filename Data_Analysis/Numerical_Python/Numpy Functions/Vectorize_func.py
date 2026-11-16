import matplotlib.pyplot as plt
import numpy as np
import math

a = np.array([1, 2, 3, 4])
# print(a**2)

x = np.arange(-2, 2, 0.1)
y = x * np.exp(-(x**2))

plt.plot(x, y)
plt.grid()
# plt.show()

# As NumPy functions are vectorized the argument of numpy fuction can be any scaler or iterable object.

l = [x for x in range(-2, 2, 1)]
L = np.sin(l)
# print(L)

x = np.random.uniform(0,10,5)
# x1 = np.ceil(x)
# x2 = np.floor(x)
# print(x2)

# Vectorize a function 
# A user function is not vectorized.
# But we can vectorize it with the NumPy vectorize()

def f(x):
    return x**3
f = np.vectorize(f)
x = [1,2,3,4]
# print(f(x))

s = np.vectorize(math.sqrt)
print(s(x))