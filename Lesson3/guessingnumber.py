import random
guess = random.randrange(1,4)

print(f"Hello, this is a game where you need to guess the number!")
print(f"I'm thinking about a number between 1 to 3")

answer = int(input("What's you guess? "))

print(f"Your number is {answer} the number that I was thinking is {guess}")
print(f"So your guess is {answer == guess}")