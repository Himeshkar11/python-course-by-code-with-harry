# generators in python 
# generatot is basically a opbject which is used to  generate some iterable values 
# this generator is used to manage memory effieceinlty 
# it is  capable of creating the desired results by iteration and can be used when necessary 
# def gen(n):
#     for i in range(n):
#         yield i 
        # the keyword key word yeild is used to generate a generator 
# inside a function  ther can be three types 
# 1. print - this prints into console ie terminal 
# 2. return - this assignes the value to the functions and stops it 
# 3. yeild - this is used to genrerate a Generator  
# program to create a fibo seq via generators 
def genfibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in genfibo(11):
    print(num)
def genfac(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact
# example 
def fun(max):
    cnt = 1
    while cnt<= max:
        yield cnt
        cnt +=1

ctr = fun(5)
for n in ctr:
     print(n)
# generator expression 
# onw liine to create a generator 
# name = (expression for iterator in range(iterable ))
sq = (x*x for x in range(1,6))
for i in sq:
    print(i)

