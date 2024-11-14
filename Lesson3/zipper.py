from shutil import make_archive
import random

filename = f"zipped{random.randrange(1,101)}"

folder = input("input your file : ")
make_archive(f"{filename}", "zip",folder)
print("Archive successful")