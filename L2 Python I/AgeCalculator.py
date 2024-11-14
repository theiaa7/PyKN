current_year = 2024

print("Hello, this is your age calculator.\n")

year = int(input("Please enter your year of birth : "))

# the code below is usual variable storing
# current_age = current_year - year
current_year -= year

print(f"Your age is {current_year}")

import os
os.system("pause")

print(f"Are you a baby : {current_year < 3}")
os.system("pause")
print(f"Are you a kid : {current_year > 3 and current_year < 10}")
os.system("pause")
print(f"Are you a teenager : {current_year > 11 and current_year < 20}")
os.system("pause")
print(f"Are you an adult : {current_year > 20}")