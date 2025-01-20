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

# words = ["banana", "apple", "blueberry", "cherry", "blackberry"]

# count = 0
# for word in words:
#     if word.startswith('b'):
#         print(word)
#         count += 1
# print(f"Total words startng with 'b': {count} ")

## Challenge 8: Count Vowels in a string

# text = "Python is an amazing programming language!"

# vowels = "aeiou"

# count = 0

# for char in text:
#     if char.lower() in vowels:
#         count += 1

# print("Number of vowels:", count)

## Challenge 9: Fibonacci Sequence -> Write a loop to print first 10 numbers in the fiboncci sequence

# a, b = 0, 1  # Initialize the first two numbers

# for i in range(10): # Loop 10 times for the first 10 numbers
#     print(a)
#     a, b = b, a + b

## Challenge 10: Nested loop - star Pattern

    #Output
    # *
    # **
    # ***
    # ****
    # *****

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()
   

## Challenge 11: Reverse a string

# text = "Python"

# for i in reversed(text):
#     print(i, end="")

# ## Challenge 12: Find the largest number

# numbers = [45, 2, 89, 32, 21, 67, 90, 12]

# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

# print(f"\nThe largest number is: {largest}")

# # Using the max function

# largestNum = max(numbers)

# print(f"The largest number is: {largestNum}")

## Challenge 13: Palindrome or not

# text = input("Enter a string: ")

# normalized_text = text.lower().replace(" ", " ")


# # is_palindrome = True
# # for i in range(len(normalized_text) // 2):
# #     if normalized_text[i] != normalized_text[-(i + 1)]:
# #         is_palindrome = False
# #         break

# # if is_palindrome == True:
# #     print(f"The palindrome {text} is True")
# # else:
# #     print(f"The palindrome is false")


#  ## Method 2: Simple comparison

# if normalized_text == normalized_text[::-1]:
#     print(f"{text} is Palindrome.")
# else:
#     print(f'{text} is not a palindrome')

## Challenge 14: Print a Number Triangle
n = int(input("Enter the number of rows for the number triangle: "))

for row in range(1, n + 1):
    for num in range(row, 0, - 1):
        print(num, end='')
    print()        
    




