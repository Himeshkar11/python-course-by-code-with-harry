# os module in python 
import os
# it is an bulit in module in python 
# print(dir(os))
# 1. current working directory
# this is used to get the path of current directory 
print(os.getcwd())
# 2. we can also change the cwd in python for the better access of files 
# os.chdir("c://")
print(os.getcwd())
# 3. list dir --> gives every file of the cwd
print(os.listdir())
print(os.listdir("D://"))
os.mkdir("Code")
# to make multiple directories 
os.makedirs("This/that/cwh")
# renaming the directories or files
os.rename("himi.txt","Himeshkar.txt")
# to join two paths in a optimal way 
print(os.path.join("C://","sonti.txt"))
# one more importatn function to check if the directory exists or not 
print(os.path.exists("C://"))
print(os.path.exists("D:// 01study"))
