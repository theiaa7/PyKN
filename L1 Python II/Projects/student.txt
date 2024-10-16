class students:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.hobby = ""
        self.lesson = ""

    def intro(self):
        print(f"Hello my name is {self.name}")
        print(f"I am {self.age}years old")
        print(f"My hobby is {self.hobby}")
        print(f"I currently learning {self.lesson}")

# initializing new object from a class
studentA = students()
studentB = students()

# assigning object attribute
studentA.name = "Jason"
studentA.age = 14
studentA.hobby = "Gaming"
studentA.lesson = "Python"

studentB.name = "Eve"
studentB.age = 15
studentB.hobby = "Singing"
studentB.lesson = "2D Games"

q = input("Type the student name : ")
if q == "Jason":
    studentA.intro()
elif q == "Eve":
    studentB.intro()