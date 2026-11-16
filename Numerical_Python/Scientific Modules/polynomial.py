import numpy as np
import numpy.polynomial as poly

p = poly.Polynomial([1, 2, 3], domain=[-1, 2], window=[-1, 1])
# p1 = np.poly1d([1, 2, 3])
# print(p)
# print(type(p))
# print(p.domain)
# print(p.window)

# print(dir(poly))

x = np.array([1, 2, 3, 4, 5])
y = np.array([20, 35, 50, 65, 80])

coeff = np.polyfit(x, y, 1)
# print(coeff)

predict = np.polyval(coeff, 6)
# print(predict)

# NOTE -
# polyfit() → Finds polynomial coefficients from data.
# polyval() → Uses coefficients to calculate polynomial values.

# Polynomial.fit()

x = np.array([1, 2, 3, 4, 5])
y = np.array([20, 35, 50, 65, 80])

P = poly.Polynomial.fit(x, y, 1)
# print(P(6))
# print(P.convert().coef)

# 1.Chebyshev polynomials
# Interval: [-1,1]
# Weight: \(w(x)=1/\sqrt{1-x^2}\)
# Used in polynomial approximation and numerical analysis.

t0 = poly.Chebyshev.basis(0)
t1 = poly.Chebyshev.basis(1)
t2 = poly.Chebyshev.basis(2)
t3 = poly.Chebyshev.basis(3)

# print(t0)
# print(t1)
# print(t2)
# print(t3.convert(kind=poly.Polynomial))

# 2.Legendre polynomials
# - Interval: \([-1,1]\)
# - Weight: \(w(x)=1\)
# - Used in spherical harmonics and solving physical problems.

# for i in range(5):
#     l = poly.Legendre.basis(i)
#     print(l)

# 3.Hermite polynomials
# - Interval: \((-\infty,\infty)\)
# - Weight: \(w(x)=e^{-x^2}\)
# - Used in the quantum harmonic oscillator and probability-related mathematics.

# for i in range(5):
#     h = poly.Hermite.basis(i)
#     print(h)

# 4.Laguerre polynomials
# - Interval: \([0,\infty)\)
# - Weight: \(w(x)=e^{-x}\)
# - Used in quantum mechanics and differential equations.

# for i in range(5):
#     l = poly.Laguerre.basis(i)
#     print(l)
