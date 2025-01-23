# my_list = []

# my_list = [1, "hello", 3.13, True]

# # Accessing Elements
# #Indexing
# print(my_list[2], my_list[0], my_list[1])

# #Slicing
# print(my_list[1:3])

# # Changing element
# my_list[1] = 5
# print(my_list[1])

# # Add elements
# my_list.append(40)
# print(my_list)

# # Insert at specific index
# my_list.insert(2, 18)
# print(my_list)

# Removing an element
# my_list.remove(5)
# print(my_list)

# my_list.pop()
# print(my_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers.remove(6)
# numbers.append(15)
# numbers.reverse()
# print(numbers)

# odd = []
# even = []

# for i in numbers:
#     if i % 2 != 0:
#         odd.append(i)
#     else:
#         even.append(i)

# print(odd)
# print(even)

# Find Minimum and Maximum

def find_min_max(numbers):
    if not numbers:
        return None, None
    
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

min_num, max_num = find_min_max(numbers)
print("Minimum: ", min_num)
print("Maximum: ", max_num)

# Frequency count

def count_frequency(numbers):
    # Create an empty dictionary to store the counts
    frequency = {}
    for num in numbers:
        # if the number is already in the dict increase the count by +1
        if num in frequency:
            frequency[num] += 1
        # if not then add it with count 1
        else:
            frequency[num] = 1
    return frequency

frequency = count_frequency(numbers)
print(frequency)
    

