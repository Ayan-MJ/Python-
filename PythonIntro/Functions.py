# Function without parameters

def say_hello():
    print("Hello World")

say_hello()

# Function with parameters

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Ayan")

# Function with return Values

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 7)
print(result)

# Default Parameter

def greet(name="User"):
    print(f"Hello, {name}")

greet()
greet("Ayan")

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Ayan")

# Find number is even or not

def is_even(number):
    if number % 2 == 0:
        return True
    return False

num = int(input("Enter number: "))
if is_even(num):
    print(f"{num} is even.")
    def factorial(num):
        result = 1
        for i in range(1, num+1):
            result *= i
        return result
    print(factorial(num))
else:
    print(f"{num} is odd.")

# Factorial of a Number
# if is_even == 0:
#     def factorial(is_even):
#         result = 1
#         for i in range(1, is_even+1):
#             result *= i
#         return result
#     print(factorial(6))
# else:
#     print("Nothing")

# Find the maximum of three numbers

def find_max(a, b, c):
    return max(a, b, c)

a = int(input("Enter no. "))
b = int(input("Enter no. "))
c = int(input("Enter no. "))

print(find_max(a, b, c))

# Calculate the sum of Digits

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

print(sum_of_digits(123)) 






