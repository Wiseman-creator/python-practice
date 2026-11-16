import numpy as np

x = np.random.uniform(-1 ,1, 1000)
y = np.random.uniform(-1 ,1, 1000)
z = x**2 + y**2 < 1
pi = 4 * np.sum(z)/1000

print("Pi estimated: ", pi)
print("pi absolute: ", np.pi)
print("Error:", abs(np.pi - pi))