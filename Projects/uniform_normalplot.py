import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0, 1, 1000000)
y = np.random.randn(1000000)

fig, ax = plt.subplots(1, 2, figsize=(12, 4))

ax[0].hist(x, bins=20, ec="k")
ax[0].set_title("Uniform Distribution")

ax[1].hist(y, bins=20, ec="k")
ax[1].set_title("Standard Normal Distribution")

plt.tight_layout()
plt.show()
