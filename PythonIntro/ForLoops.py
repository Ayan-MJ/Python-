## Challenge 1. Reverse a list

# fruits = ["apple", "banans", "cherry"]

# for fruit in reversed(fruits):
#     print(fruit)

## Challenge 2. Find Even Numbers in a Range of 1 to 20

# for number in range (2, 21, 2):
#     print(number, end=" ") # print all the numbers on one line

## Challenge 3: Sum of Numbers

# numbers = [3, 7, 12, 19, 21]

# total = 0

# for number in numbers:
#     total += number

# print("\nSum: " , total)

## Challenge 4: Nested loop Multiplication table of 1 to 3 numbers

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} * {j} = {i * j}")

# ## Challenge 5: Occurence of letter 'a' in the lsit of strings

# words = ["apple", "banana", "grape", "avocado"]

# count = 0

# for word in words:
#     count += word.count('a') # use .count() to count 'a' in each word

# print(f"The letter a appears {count} times.")

## Challenge 6: Square of Numbers

# for number in range(1, 11):
#     square = number * number
#     print(square, end='')

## Challenge 7: Filter words Write a loop to print words from a list that start with the letter 'b'.

words = ["banana", "apple", "blueberry", "cherry", "blackberry"]

count = 0
for word in words:
    if word.startswith('b'):
        print(word)
        count += 1
print(f"Total words startng with 'b': {count} ")