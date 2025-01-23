# Problem 1: Word Frequency Counter

def word_frequency(text):
    # We convert the text into words by using .split()
    words = text.split()
    # We store the words in a dictionary by creating an empty dictionary
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


text = "hello world hello"
print(word_frequency(text))

# Problem 2: Merge two dictionaries

def merge_dicts(dict1, dict2):
    merged = dict1 | dict2
    dict1.update(dict2)
    return merged

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))

# Problems 3: Invert a dictionary

my_dict = {"a": 1, "b": 2, "c": 3}

# Use a dictionary comprehension to swap keys and values

def inver_dict(my_dict):
    return {value: key for key, value in my_dict.items()}

my_dict = {"a": 1, "b": 2, "c": 3}
print(inver_dict(my_dict))

# Problems 4: Check for key Existence

def check_key(my_dict, key, default):
    return my_dict.get(key, default)


my_dict = {"name": "Alice", "age": 25}
key = "age"
default = "Unknown"
print(check_key(my_dict, key, default))

# Problem 5: Nested Dictionary Access
# Write a function that takes a nested dictionary and a list of keys, and returns the value at the specified path. If any key in the path doesn't exist, return None.

    