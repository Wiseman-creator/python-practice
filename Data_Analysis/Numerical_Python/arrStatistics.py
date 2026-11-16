import numpy as np

x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
y = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# sum over arrays

print(x.sum())
print(y.sum(0))
print(y.sum(1))

# Cumulative sum or cumsum()

x0 = np.cumsum(x)
print(x)
print(x0)

y0 = np.cumsum(y, axis=0)
print(y)
print(y0)

print(y.cumsum(1))  # Along axes = 1

# Minimum, Maximum

print(x.min(), x.max())
print(y.min(0), y.max(0))
print(y.min(1), y.max(1))

# Mean, Median

print(y.mean(0))
print(y.mean())

med = np.median(y, axis=0)
print(med)

# Variance, Standard Variation & peak-to-peak

a = np.array([2, 4, 3, 5, 1, 6, 4, 3, 2])
b = np.array([[2, 4, 3], [5, 1, 6], [4, 3, 2]])

print(a.var())
print(a.std())
p = np.ptp(a)
print(p)

print(b.var(0))
print(b.std(0))
print(b.var(1))
print(b.std(1))

# Covariance & Correlation coefficient

m = np.random.uniform(0, 1, 1000)
n = np.random.uniform(0, 1, 1000)

print(np.cov(m, n))
print(np.corrcoef(m, n))
