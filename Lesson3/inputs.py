import random

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

print(f"This program will randomize between {num1} to {num2-1}")

number = random.randrange(num1,num2) #num 1 = 1, num2 = 101

print(f"The random number generated is {number}")