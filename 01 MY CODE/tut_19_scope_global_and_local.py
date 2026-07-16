# l = 10 # this is a global variable
# def function1(n):
#     l = 5#this is a local variable
#     m = 8
#     print(n,"i have printed")
#     print(l,m) # will search for local first
# function1("hello himi")
# print(l) #this will print only global and local ni assalu dekadhu
# # print(m) #therfore this wil throw an error
# # we cant change the value of global variable in a function but we can if we use
# # global keyword
# l = 10 # this is a global variable
# def function2(n):
#     # l = 5#this is a local variable
#     m = 8
#     global l
#     l = 45# this will change the global variable value
#     print(n,"i have printed")
#     print(l,m) # will search for local first
# function2("hello himi")


def himi():
    x = 20
    def luffy():
        global x
        x = 56
    # print("Hey luffy ",x) # this global will not change the value of x because global always goes out of the function ie to start

    luffy()
    print("hey lufyy",x)
himi()
print(x)
