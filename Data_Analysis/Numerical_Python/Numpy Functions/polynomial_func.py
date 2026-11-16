import matplotlib.pyplot as plt
import numpy as np

# Polynomial function in NumPy
# 1D polynomial class, poly1d() creates a 1D polynomial.
# To construct a polynomial x^2 + 2x + 3 through the function, we must give the list of coeffcients as argument.

p = np.poly1d([1, 2, 3])

print(type(p))  # <class 'numpy.poly1d'>
print(p(0))  # 3

print(p.r)

p1 = np.poly1d([1, 2, 3])
p2 = np.poly1d([1, -2])

print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
print(p1 / p2)

f = np.poly1d([1, 2])  # f(x) = x + 2
print(f * f)
print(f**2 + np.sin(f))

# Plotting of a polynomial function

P = np.poly1d([1, -5, 6])
x = np.linspace(1, 4, 100)
plt.plot(x, P(x), lw=3)
plt.axhline(
    linestyle="--",
)
plt.grid()
plt.show()

print(p.deriv())
print(p.deriv(1))
print(p.integ())
print(p.integ(2))
