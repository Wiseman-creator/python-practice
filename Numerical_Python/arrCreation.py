import numpy as np

# 1. Range of numbers
a = np.arange(2, 10, 2)
print(a)

a = np.arange(2, 10)
print(a)

a = np.arange(10)
print(a)

b = np.arange(0, 5.0, 0.5)
print(b)

# Unlike the range() in core python arange() can create fractional numbers or floats.


# 2. Linear Space

# SYNTAX --- linspace(start, end, num)

l = np.linspace(10, 20, 5)  # step_size = (20-10)/4 = 2.5
print(l)

l = np.linspace(10, 20, 5, endpoint=True)
print(l)

l = np.linspace(10, 20, 5, endpoint=False, retstep=True, dtype=int)
print(l)

# 3. Logarithmic Space

# SYNTAX --- logspace(start, end, num)

lg = np.logspace(0.1, 1, 5)  # Default Base = 10
print(lg)

lg1 = np.logspace(0.2, 1, 4)
print(lg1)

lg2 = np.logspace(0.2, 1, 4, base=2)
print(lg2)
