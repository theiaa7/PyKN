import random

num = random.randrange(1,101)

print("Hello, this is random number generator!")
print("We have a value between 1 - 100")
print("If the value is less than 50, we will let you know")

if num < 50:
    print(f"The value of num is {num} which less than 50")

if num > 90:
    print(f"The value is so high its {num}")

print(f"The number is {num}")
