# Program to read a file (ask for filename) and handle FileNotFoundError with try-except
try:
    a = input("enter the file name here :")
    f = open("a","r+")
    f.read()
    f.close()
except FileNotFoundError:
    print("file not found please try again!",FileNotFoundError)
print("kbvb")