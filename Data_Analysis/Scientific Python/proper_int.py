import numpy as np
from scipy.integrate import quad, simpson

# print(dir(scipy.integrate))

# Proper integral 
# 1. Integration by Gauss quadrature
f = lambda x: x**2

intG = quad(f, 0, 2)    # quad(func, lower_limit, upper_limit)
print(intG)     # (value, error)

# 1. Integration by Simpson's rule

x = np.linspace(0, 2, 1000)

intS = simpson(f(x), x)

print(intS)
# NOTE --- the arguments in simpson() func are the integrand func f(x) 
# and the array of x (array of equidistant points between the integration limits.)
