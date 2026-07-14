# comprehensions are a short way of crreating a data structure in python 
# if we want to create a list of numbers ranging from 1 to 99 then 
# this ishow i used to do it 
# there are usually 4 types of comprehensions 
# 1. list comprehension 
# 2. dictionary comprehension
# 3. set comprehensions 
# 4. generator comprehensions
ls = []
for i in range(100):
    ls.append(i)
print(ls)
print("With list comprehensions")
lis = [i for i in range(100)]
print(lis)
# similarly for returning a list of odd numbers in the range 100 
odd = [i for i in range(100) if i%2!=0]
print(odd)
# ls = [expression kaha_tak condition] list comprehension syntax 
# //////// dictionary comprehension
# eg : - 
# we want to create a dcitonary which looks like the dict1 below
dict1 ={0:"item0",1:"item1",2:"item2"} # till 100 or multiple indices
dict2 ={i:f"item {i}" for i in range(100)}
print(dict2)
# the syntax is similar to list comprehensions but the only change here is 
# the key value pairs 
# {key:value kitna_chahiye condition}
# this comprehensions are not only a good to createa  dictionary but also to 
# reverse the key value pairs
dict3 = {i:f"Item{i}" for i in range(5)} 
dict3 = {value:key for key,value in dict3.items()}
print(dict3)# this reverses the dict3 completely

# set comprehensions
# here the concept is same as list comprehension but the values which are same or repeated will be avoided/
dresses = {dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}
print(dresses)
# will print the dress 1 and dress2 only once not like list comprehension

# generator comprehensions
evens = (i for i in range(100) if i%2==0)
print(type(evens))
# print(evens) # generaotr object is created 
# for i in evens: # testing the generator
#     print(i)
print(evens.__next__()) # will print the next value of the generator 
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
# question from harri bai : 
# take the number of elements input and using for loop take input of all those 
# ask the user which comprehension to be made 
# create the comprehension for the user 


