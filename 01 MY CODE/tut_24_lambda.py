# def minus(a,b):
#     return a-b
# print(minus(10,2))

# when we dont have the need to define a whole function we use lambda function
# minus = lambda a,b : a-b
# print(minus(10,2))
# it is a one liner function which can be used instead of function
# but it cant do higher level of logic
# it used with various functions like map , filter and sort and each have a very diiferent function
print(list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,8])))