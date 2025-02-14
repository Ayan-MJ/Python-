import numpy as np
from numpy.ma.core import reshape

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Addition arrays
print(a + b)

# Multiplying arrays
print(a * b)

# Or adding a single number to all elements
print(5 * a)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # (2, 3) meaning 2 rows, 3 columns

reshaped_arr = arr.reshape(3, 2)
print(reshaped_arr)