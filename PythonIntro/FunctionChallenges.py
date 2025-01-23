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

num = []
