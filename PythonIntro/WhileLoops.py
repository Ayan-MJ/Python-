import time
import random
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# Challenge 1: Count down 

# count = int(input("Enter the starting number for the countdown: "))
# if count > 0:
#     temp = count
#     print("\nOptions:")
#     print("1. Countdown")
#     print("2. Reverse countdown")
#     print("3. Both countdown and reverse countdown")
#     choice = input("Choose an option (1/2/3): ")

#     if choice == "1" or choice == "3":
#         print("\nCounting down:")
#         while count >= 1:
#             print(f"Counting down: {count}")
#             count -= 1  # decreases the value of count by 1 after each iteration.
#             time.sleep(1)
#         print("Blast off!")

#     # Reverse Countdown
#     if choice == "2" or choice == "3":
#         print("\nCounting Back up:")
#         for i in range(1, temp + 1): 
#             print(f"Counting up: {i}")
#             time.sleep(1)
# else:
#     print("Please enter a Positive number")

# Challenge 2: Sum of Numbers

# n = int(input("Enter your number: "))
# total_sum = 0

# while n != 0:
#     digit = n % 10   # Extract the last digit
#     total_sum += digit
#     n = n // 10

# print(total_sum)

secret_number = random.randint(1, 100)

print("I have chosen a number between 1 to 100. Can you guess it?")
guess = None

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try agian.")
    else:
        print(f"Congratualtions! You guessed the number: {secret_number}")







