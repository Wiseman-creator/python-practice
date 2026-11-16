import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 1000)
y = np.linspace(-1, 1, 1000)

X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 + Y**2)
# Z = np.sin(X) * np.cos(Y)
# Z = np.exp(-(X**2 + Y**2))

# plt.contour(X, Y, Z)
# plt.show()

contours = plt.contourf(X, Y, Z, levels=30, cmap='viridis')

plt.colorbar(contours, label='Z values')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(r'$z=e^{-x^2+y^2}$')

plt.show()