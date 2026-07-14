# numbers = ["12","10","56"]
# #
# # for i in range(len(numbers)):
# #     numbers[i] = int(numbers[i]) # doing this will convert each string element into a integer element
# #
# # numbers[1] = numbers[1]+46
# # print(numbers[1])
#
# # we dont always want to write the complete code when we can write in a line
# # map() this function is very useful for applying a function over a list or tuple it is like a facotry
# numbers = list(map(int,numbers))
# print(numbers) # it will return <map object at 0x000001AD131EE920> this therfore we need to type cast it as a list thie printed ones shows in whcih location is the objects stored
#
# num = [1,2,3,56,65,69,4]
# # def sq(a):
# #     return a*a
# # num = list(map(sq,num))
# # print(num)
#
# # we can use lambda that one liner anonymus function to do this
# num = list(map( lambda x:x*x,num))
# print(num)
def sq(a):
    return a*a
def cube(a):
    return a*a*a
func = [sq,cube]
for i in range(5):
    v = list(map(lambda x:x(i),func))
    print(v)
list_1 = [1,2,3,4,5,6,7,8,9,10]
def is_greaterthan5(num):
    return num>5
v = tuple(filter(is_greaterthan5,list_1))
print(v)

from functools import  reduce
summ = [1,2,3,4,5]
v = reduce (lambda x,y:x+y,summ)
print(v)