print("Hello, Ayan!")

name = input("Enter your name: ") 
age = input("Height: ")
height = input("Age: ")


print("Hello, " + name + "! Welcome to python.")
print("Your height: " + height)
print("Age: " + age)

x = 99
y = 77

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

#Conditional Statements
number = int(input("Enter the number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("negative")
else:
    print("Zero")


#Odd or even
num = int(input("Enter the number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
