
print("hello")
print("I need you to type the color of traffic light \n1. red \n2. yellow \n3. green")

color = input("Please enter the color that you see : ")

if color == "red":
    print("stop, its a red light, wait until you got a green!")
elif color == "yellow":
    print("becareful, light are changing, pay attention!")
elif color == "green":
    print("its green now, you can go!")
else:
    print(f"{color} is not a color in a traffic light, restart the program!")
