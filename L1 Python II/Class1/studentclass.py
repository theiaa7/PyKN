class student:
    # initialize the structure of the object
    def __init__(self):
        self.name = ""
        self.age = 0
        self.hobby = ""
        self.lesson = ""

    # make the methods for the class objects
    def intro(self):
        print(f"Hello, my name is {self.name}")
        print(f"I am {self.age}years old")
        print(f"My hobby is {self.hobby}")
        print(f"I'm currently learning {self.lesson}")

# initializing objects
student1 = student()
student2 = student()

# assigning object attribute
student1.name = "Jason"
student1.age = 14
student1.hobby = "Gaming"
student1.lesson = "Python"

student2.name = "Eve"
student2.age = 15
student2.hobby = "Singing"
student2.lesson = "Python"

q = input("What is the student name? ")
if q == "Jason":
    student1.intro()
elif q == "Eve":
    student2.intro()
else:
    print("Student doesn't exist")