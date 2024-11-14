num1 = 5
num2 = 3

eq1 = num1 + num2
eq2 = num1 - num2
eq3 = num1 * num2
eq4 = num1 / num2
eq5 = num1 % num2
eq6 = num1 ** num2

print(f"{num1} + {num2} = {eq1}")
print(f"{num1} - {num2} = {eq2}")
print(f"{num1} * {num2} = {eq3}")
print(f"{num1} / {num2} = {round(eq4, 2)}")
print(f"{num1} % {num2} = {eq5}")
print(f"{num1} ** {num2} = {eq6}")

roundvalue = "{:.4f}"
division = roundvalue.format(eq4)
print(division)
rounded = round(eq4, 2)
print(rounded)
