# Random walk in 2D

import random as rd
import matplotlib.pyplot as plt

x,y = 0,0
X,Y = [],[]

incrementList = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(100):
    dx, dy = rd.choice(incrementList)
    x = x+dx
    y = y+dy
    X.append(x)
    Y.append(y)

plt.plot(X,Y)
plt.show()