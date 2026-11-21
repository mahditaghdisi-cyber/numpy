import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0])
print(a[-1])
print(a[1:4])
print(a[:3])
print(a[2:])

b = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(b[0, 0])
print(b[1, 2])
print(b[0])
print(b[:, 1])
print(b[1, :])