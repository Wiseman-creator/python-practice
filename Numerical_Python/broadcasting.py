import numpy as np

x = np.arange(1,10).reshape(3,3)

y = 10
print(x+y)

y2 = np.array([1,11,111])
print(x+y2)

y_c = np.array([[10],[11],[12]])
print(x+y_c)