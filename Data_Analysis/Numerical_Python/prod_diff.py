import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, -1, -2])
print(x.prod())

y = np.arange(1, 6)
print(y.prod())

print(np.diff(x))

"""Consider the following y vs x data, a sigmoidial curve created through NumPy function and array for demonstration. The first derivative z equal to dy/dx is computed through np.diff()"""
x = np.linspace(-5, 5, 100)
y = 1.0 / (1 + np.exp(-x))
z = np.diff(y) / np.diff(x)

plt.subplot(211)
plt.plot(x, y)
plt.subplot(212)
x_diff = (x[:-1] + x[1:]) / 2

plt.plot(x, y, label="Sigmoid")
plt.plot(x_diff, z, label="First derivative")
plt.legend()
plt.grid()
plt.show()
