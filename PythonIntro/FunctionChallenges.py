# Problem 1: Find the square of a Number

def is_Square(num):
    square = num * num
    print(square)

is_Square(5)
is_Square(8)

# Check if a Number is Positive, Negative, or Zero

def number(num):
    if num < 0:
        print("Negative")
    elif num > 0:
        print("Positive")
    elif num == 0:
        print("Zero")

n = int(input("Enter number: "))
number(n)

# Calculate the Sum of a list

def sum(num):
    total = 0
    for i in num:
        total += i
    print(total)

num = [8, 9, 22, 5, 2]

sum(num)

