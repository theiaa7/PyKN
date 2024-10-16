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

    def show(self):
        print("Hi my name is ", self.owner)
        print("My house has ", self.color, " color")
        print("With width : ", self.width, "Length", self.length, "Height:", self.height)
        print("It has :", self.bedroom, " bed room", self.bathroom, " bathroom")


# House Type A
# Input value
typeA = house()
typeA.owner = "Budi"
typeA.color = "Blue"
typeA.width = 100
typeA.length = 150
typeA.height = 200
typeA.bedroom = 4
typeA.bathroom = 2
# call method show
typeA.show()

# House Type B
# Copy TypeA and change the value as you want
typeB = house()
typeB.owner = "Raisa"
typeB.color = "Pink"
typeB.width = 250
typeB.length = 350
typeB.height = 450
typeB.bedroom = 6
typeB.bathroom = 1

typeB.show()

# Calculate the area using square formula
AreaA = typeA.width * typeA.length * typeA.height
AreaB = typeB.width * typeB.length * typeB.height


def compare():
    if AreaA < AreaB:
        print(typeA.owner, "'s House is smaller than ", typeB.owner, " House")
    else:
        print(typeB.owner, "'s House is smaller than ", typeA.owner, " House")


compare()
