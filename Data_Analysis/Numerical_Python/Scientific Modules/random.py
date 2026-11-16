import numpy as np

x = np.random.random()
# print(x)    # For generating a random number in 0 and 1

x_arr =  np.random.random(size=10)
# print(x_arr)

x_arr34 =  np.random.random((3,3))
# print(x_arr34)

# Uniform Distribution

y = np.random.uniform(0.5,1, size=10)
# print(y)

# Normal Distribution

n = np.random.randn(100000)     # mean = 0, S.D = 1
m = np.random.normal(0.5, 2, 100000)

print(n)
print(m)