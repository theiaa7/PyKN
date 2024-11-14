
print("Hello, this is a username validator. We will check if your username is qualified to our standards")
print("Our username standards are : \n1. The username characters need to be more than 5 but no more than 10")
print("2. the username should be all lowcase")

username = input("Username Input : ")

if len(username) < 5 or len(username) >= 10:
    print("Username is too short!")
elif not username.islower():
    print("Character need to be lowercase, not capital!")
else:
    print(f"Username {username} is valid and qualified!")