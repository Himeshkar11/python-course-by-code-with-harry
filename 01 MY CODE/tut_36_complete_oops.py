# ********************** intro to class and object ************************
# class is the blueprint for creating objects
# object is the instance of a class
# creating a class 
# the class here created is called student under which name is an attribute

class Student:
    name = "himesh"
s1 = Student() #this is called creating the object (instance)
print(s1.name)
s2 = Student() # now we are creating one more object(instance)
print(s2.name)
# the below is another class named car
class Car :
    color = "red"
    type = "autogear"
    brand = "volkswagen"
    seats = "5"
# this class has attributes color type brand and seats 
car1modelfb = Car() # creating a new car named car1modelfb
print(car1modelfb.color,car1modelfb.type,car1modelfb.brand)

# ********************** __init__(self)  and self methods************************
# constructor : all classes have a function callled __init__ which is always executed when the class is being intiaed 
# it is a self calling function 

# types of constructors 

# 1. default constructor these are those constructors which has only sing parameter "self". if we dont write this in python it will do it automatically 
# 2. parameterizzed construction 
# these are those constructors which has attributes other than self 
class Pokemon:
    def __init__(self,type,level):
        self.type=type
        self.level=level
p1 = Pokemon("fire",69)
print(p1.type,p1.level)
# if we have more than one construction in the same class then the one which matches or attributes will be executed,
# generally as such we dont make many constructiors we see the need and make them acc to need 
a = input("Enter your Name here:")
b = input("Enter your rank here:")
c = input("Enter your brach here:")
class Student:
    clg_name = "IIT Tokyo"
    def __init__(self,name,rank,branch):
        self.name = name
        self.rank = rank
        self.branch = branch
    def hello(self): # this is called methods 
        print("Hello yarou",self.clg_name)
# s3 = Student(a,b,c)
# print(s3.hello)
# print(s3.name,s3.clg_name,s3.rank)

# ********************** using functions inside class ************************
        
s1 = Student(a,b,c) 
s1.hello()
print(s1.name,s1.rank,s1.branch,s1.clg_name)
# Let's Practice
# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
class Student:
    print("WELCOME TO THE SYSTEM ......")
    def __init__(self,name,marks_sub1,marks_sub2,marks_sub3):
        self.name=name
        self.marks_sub1=marks_sub1
        self.marks_sub2=marks_sub2
        self.marks_sub3=marks_sub3
    def Average_marks(self):
        avg = (self.marks_sub1 + self.marks_sub2 + self.marks_sub3)/3
        print(avg)
  
marks_sub1=int(input("Enter the marks of sub1 here :"))
marks_sub2=int(input("Enter the marks of sub2 here :"))
marks_sub3=int(input("Enter the marks of sub3 here :"))
s1 = Student("HIMESH",marks_sub1,marks_sub2,marks_sub3)
a = s1.Average_marks
s1.Average_marks() 
# ********************** class methods ************************
# usually every class has some data and methodss 
# whenever we use methods in class always make the first parameter should be self
# here the below code take the name via the argument of object 
# and class has a method to save the name 
class Student:
    def __init__(self,fullname):
        self.name=fullname
        
s1=Student("kyokun")
print(s1.name)

s1.name = "kyoronin" # this way i can change the value of the attribute after making the object 
print(s1.name)
# static methods : these are those methods that dont use the self parameter 
# these are generally used to print a static messages 
# these are genrally done using decorators 
#__________ decorators allows us to wrap another function in order to extend the behaviour of the wrapped function without permananetly modifing it

class Anime:
    @classmethod
    def yokoso():
        print("Yokoso watashi no soul society ee ")
    def __init__(self,name,fav_anime,fav_chara):
        self.name = name 
        self.fav_anime = fav_anime 
        self.fav_chara = fav_chara 
# there are four pillars of object oriented programming 
# they are 
# 1. Abstarction 
# 2. Inheritance 
# 3.Poly morphism
# 4. encapsulation

# ********************** Abstraction ************************
# it is the concept of hinf=ding the implementation details of a class and only showing the essential features
# it uses abstract classes via abc classes 
# from abc import ABC,abstractmethod
# Class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# abstract classes :-
# what is an abstract class 
# .. class that cannot be instantiaed directly
# .. used t define a common interface for all it`s subclasses 
# .. created using the abc module(ABC class)`

    
    
# class Car :
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.acc = True
#         self.clutch= False
#         print("the car started ......")
# c1=Car()
# c1.start()
# ********************** practice question 
# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance. MY TRY"************************
# credit_me = int(input("Enter your credit here :"))
# debit_me = int(input("Enter your debit here :"))
# class Account:
#             @classmethod
#             def debit(debit_me):
#                 print(debit_me)
#             @classmethod
#             def debit(credit_me):
#                 print(credit_me)
#             @classmethod
#             def balance(self,balance_me):
#                 balance_me = (credit_me- debit_me)
#                 print(f"SO your balance is{balance_me} ...... ")
#             def __init__(self,account_no,balance):
#                 self.balance= balance
#                 self.account_no= account_no

    
   # ***********************MY TRY time 2 "************************
# class Account:
#     def __init__(self,balance,acc_no):
#         self.balance=balance
#         self.acc_no=acc_no
    
#     def add_money(self,credit):
#         self.balance= self.balance+credit
#         print(f"the amount{credit} was taken from your account")
#     def take_money(self,debit):
#         self.balance = self.balance-debit
    
#     def bal_print(self):
#         print(f"the balance in the account is {self.balance}")
# takashi = Account(10000,"456as")
# takashi.add_money(456)
# takashi.take_money(50)
# takashi.bal_print()

# ***********************OOPS PART 2 "************************
# ***********************del  "************************
# this is used to delete complete class or just a instance under class
# class Student:
#     def __init__(self,name):
#         self.name = name
# s1 = Student("Himesh")
# print(s1.name)
# del s1.name
# print(s1.name) # will throw a err because s1 is deleted 
# *********************** public and private attributes "************************
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass
# s1 = Account("456123789","himesh123kar")
# print(s1.acc_pass,s1.acc_no)
# this is a bad practice 
# we cant leak our password like this
# # so we use __acc_pass to not let other people see our password 
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)
# s1 = Account("456123789","himesh123kar")
# print(s1.acc_no)
# print(s1.reset_pass()) # will show an error
# *********************** public and private attributes  for methods "************************
# class Person :
#     def __hello(self):
#         print("hello person !") # is not useable under the object or out of the class 
#     def welcome(self):
#         self.__hello()
#         # we may have a doubt why are we creating a fucntion if we cant use it outside of the class 
#         # so we use this private function in a public thus restricting the user 
        
# p1 =Person()
# # print(p1.__hello()) # will give a error
# print(p1.welcome())
# *********************** inheritance  "************************
# class Car :
#     color ="white"
#     @staticmethod
#     def start():
#         print("Car started ...")
#     @staticmethod
#     def gear():
#         print("the current gear is ....")
# class Toyotacar(Car):
#     def __init__(self,name):
#         self.name =name 
# c1=Toyotacar("Fortuner")
# print(c1.start()) # we may think there might be error but it works nicely 
# ***********************types of inheritance  "************************
# ***********************multi-level inheritance  "************************

# class Car :
#     color ="white"
#     @staticmethod
#     def start():
#         print("Car started ...")
#     @staticmethod
#     def gear():
#         print("the current gear is ....")
# class Toyotacar(Car):
#     def __init__(self,name):
#         self.name =name 
# class Fortuner(Toyotacar):
#     def __init__(self,type):
#         self.type = type
# c1=Fortuner("petrol")
# print(c1.start(),c1.type)       
# ***********************multiple  inheritance  "************************
# class A:
#    varA = "This is class A"
# class B:
#    varB ="This is class B"
# class c(A,B):
#    varC = "This is class C"
# va = c()
# print(va.varA)
# print(va.varB)
# print(va.varC)
# ***********************super method  "************************
# class Car:
#    def __init__(self,type):
#       self.type = type
#    @staticmethod
#    def start():
#       print("Car started ...")
#    @staticmethod
#    def brk():
#       print("Car is on break >> ")
# class Toyotacar(Car):
#    def __init__(self,name,type):
#       self.name = name
#       super().__init__(type) # this will let us access the parents init attributes also 
   
# c1 = Toyotacar("Ronin","CNG")
# print(c1.type) # this will give me err becuase there is no modue called type in toyotacar 
# # AttributeError: 'Toyotacar' object has no attribute 'type'
# # PS C:\Users\himes> 
# # to get correct one we use super attribute 
# ***********************class and static method  "************************
# class Person:
#    name ="x"
   
#    def changeName(self,name):
#       self.name = name
# p = Person()
# p.changeName("y")
# print(p.name)
# print(Person.name) # this will be x which we dont want so 
# ............................there are many ways to resolve this 
# ///////////////////////////////method 1 
# class Person:
#    name ="x"
   
#    def changeName(self,name):
#       Person.name = name
# p = Person()
# p.changeName("y")
# print(p.name)
# print(Person.name) # now both will be printed y 

# //////////////////// method 2 
# class Person:
#    name ="x"
   
#    def changeName(self,name):
#       self.__class__.name = name
# p = Person()
# p.changeName("y")
# print(p.name)
# print(Person.name)
# //////////////////// method 3 using class method 
# class Person:
#    name ="x"
   
#    @classmethod
#    def changeName(cls,name):
#       cls.name = name 
# p = Person()
# p.changeName("y")
# print(p.name)
# print(Person.name)
# ***********************property decorator   "************************
# class Student:
#    def __init__(self,phy,chem,maths):
#       self.phy = phy
#       self.chem = chem
#       self.maths = maths
#    @property makes it look like a function which changes output each time the values area changed 
#    def avg(self):
#       return int((self.phy+self.chem+self.maths)/3)
# kyo = Student(92,78,99)
# print(kyo.avg)
# *********************** polymorphism "************************
# # the same operator + has different meanings
# print(2+3) # 5 
# print("kyo"+"ronin") # concatenate
# print([1,2,3,4,5]+[6,7,8,9,10]) # merge list 
# creating a class for complex number 
# class Complexno :
#    def __init__(self,x,y):
#       self.x =x 
#       self.y =y 
#    def __add__(self,other):
#       return Complexno(self.x+other.x , self.y+other.y)
# v1 = Complexno(4,5)
# v2 = Complexno(1,1)
# v3 = v1 + v2 
# print(v3.x,v3.y)
# *********************** practice questions  "************************
# # /////////////////////////circle question 
# class Circle:
#    def __init__(self,radius):
#       self.radius = radius
   
#    def Area(self):
#       print( (3.14)*(self.radius**2))
   
#    def Perimeter(self):
#        print((2)*(3.14)*(self.radius))
# c1 = Circle(1)
# c1.Area()
# c1.Perimeter()
# # /////////////////////////employee  question 
# class Employee:
#    def __init__(self,role,dept,salary):
#       self.role = role
#       self.dept = dept
#       self.salary = salary
#    def showDetails(self):
#       print(self.role,self.dept,self.salary,)
      
# # himi =Employee("coder","cse","10cr")
# # a = himi.showDetails()

# class Engineer(Employee):
#    def __init__(self,name,age):
#       self.name = name
#       self.age = age
#       super().__init__("Coder","Marketing",40)
   
      
# me = Engineer("17","kyo")
# print(me.salary)
# # # /////////////////////////order question 
# class Order:
#    def __init__(self,order,price):
#       self.order = order
#       self.price = price
#    def __gt__(self,other):
#       return self.price > other.price
# o1 =Order("pen",10)
# o2 = Order("pencil",5)
# print(o1>o2)
      # finally oops is over 
      
# *********************** abstract base class abc and @abstract method   "************************
# from abc import ABCMeta ,abstractmethod
# class Shape(metaclass=ABCMeta): # to tell that class is of abc 
#    @abstractmethod # to make a rule that every child should have this 
#    def printarea(self):
#       return 0
# class Rectangle(Shape):
#    def __init__(self,length,breadth):
#       self.length = length
#       self.breadth = breadth
#    # def printarea(self):
#    #    return (self.length * self.breadth)
# rec1 =Rectangle(4,5)
# # a1 = rec1.printarea()
# # print(a1)
# # TypeError: Can't instantiate abstract class Rectangle without an implementation for abstract method 'printarea' 
# # this will come because i commented out the print are which was essential as it is described using abc module
# *********************** setters and getters   "************************
# @Property this is called a property decorator useful to view private attributes
# @propertyname.setter this is called a setter can be used to change the initial values into something else 
# class Myclass:
#       def __init__(self,value):
#             self._value = value
#       @property
#       def value(self):
#             return self._value
# a = Myclass(2)
# print(a.value)
# print(a._value) # this also can be used but not recommended


# # setterss 
# class Myclass:
#       def __init__(self,value):
#             self._value = value
#       @property
#       def value(self):
#             if self._value>=18:
#                   print("eligible to watch overflow")
#             else:
#                   print( "not eligible to watch overflow \n go to sleep kid ")
#             return self._value
#       @value.setter
#       def value(self,age):
#             self._value = age
            

# if i want to print something then i should print them in @ property only 
# Because in Python setter methods are only called when you assign a value, not when you access it.

# In original code:

# print(himesh.value)


# This calls the getter, not the setter.

# the if-else in the setter never runs when printing, so no message appears.

# Putting the if-else in the getter ensures it executes whenever you read value, like with print(himesh.value).

# Summary:

# Purpose	Where it runs
# Validate/update	Setter (on assignment)
# Print/check	Getter (on access/reading)

# So to print messages dynamically, the logic must be in the getter.

# himesh = Myclass(45)
# sonti = Myclass(14)
# print(himesh.value)
# print(sonti.value)
