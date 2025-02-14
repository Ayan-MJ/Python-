import numpy as np

# A list of numbers in python
numbers_list = [1, 2, 3, 4, 5]

# Convert that list into a NumPy Array
numbers_array = np.array(numbers_list)
print(numbers_array)

zeros_array = np.zeros(5)
print(zeros_array)

# This is will create a 1D array with 5 elements with the value 1
random_array = np.random.rand(5)
print(random_array)

ints_array = np.random.randint(10, 20, 5)
print(ints_array)

# 2D Array
random_int_2d = np.random.randint(0, 10, (3, 3))
print(random_int_2d)

grid_array = np.array([[1, 2], [3, 4]])
print(grid_array)

