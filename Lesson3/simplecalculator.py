from __future__ import division
import os

print("Hi, this is an instant calculator!")
print("By using this application, you can get many result at once.")
print("Please type the 2 number needed below.")

num1 = int(input(f"First input : "))
num2 = int(input(f"second input : "))

print("Calculating now.....")
os.system("pause")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")