class house:
    def __init__(self):
        self.owner = ""
        self.color = ""
        self.material = ""
        self.width = 0
        self.length = 0
        self.height = 0
        self.bedroom = 0
        self.bathroom = 0

    def unit(self):
        print(f"The owner of the property is {self.owner}")
        print(f"The house color is {self.color}")
        print(f"Area of the house are the following measurements")
        print(f"Width : {self.width}m2")
        print(f"Length : {self.length}m2")
        print(f"Height : {self.height}m2")
        print(f"It has {self.bedroom} Bedroom, and {self.bathroom} Bathroom")

unit1 = house()
unit1.owner = "Jason"
unit1.color = "Blue"
unit1.width = 100
unit1.length = 150
unit1.height = 200
unit1.bedroom = 4
unit1.bathroom = 2

unit2 = house()
unit2.owner = "Eve"
unit2.color = "Yellow"
unit2.width = 250
unit2.length = 350
unit2.height = 300
unit2.bedroom = 8
unit2.bathroom = 3

unit1.unit()
print("=================")
unit2.unit()

# calc
Area1 = unit1.width * unit1.length * unit1.height
Area2 = unit2.width * unit2.length * unit2.height

def compare():
    if Area1 > Area2:
        print(f"House of {unit1.owner} is bigger than {unit2.owner}")
    else:
        print(f"House of {unit2.owner} is bigger than {unit1.owner}")

q = input("Do you want to compare the area and size of both unit? (1.Yes/2.No)")
if q == "1":
    compare()
else:
    print("Good bye!")