
print("Hello, we will categorize you by your age")
age = int(input("Please input your age : "))

if age < 5:
    print(f"You are {age} years old, a baby!")
elif age < 12:
    print(f"You are {age} years old, a kid!")
elif age < 18:
    print(f"You are {age} years old, a teenager!")
else:
    print(f"You are above 18, an adult!")