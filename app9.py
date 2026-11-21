import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)


numbers = np.array([10, 20, 30, 40, 50])

print(np.sum(numbers))
print(np.mean(numbers))
print(np.min(numbers))
print(np.max(numbers))
print(np.std(numbers))


a = np.array([1, 4, 9, 16])

print(np.sqrt(a))
print(np.square(a))
print(np.abs([-5, -10, 15]))