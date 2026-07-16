# creating the same employee class 
class Employee():
    # creating  a constructor to take the arguments of first name and last name 
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@codewithharry.com" # this is the problem
        # so we will comment it out first and return email in printmail function 
        # making a method inside the employee class named explain 
        # which returns a f-string
    def Explain(self):
        return f"The name of the employee is {self.fname}  {self.lname}"
    # making a method to print the email of employee
    # def printemail(self):
        # return self.email
    @property
    def printmail(self):
        if self.fname == None or self.lname == None :
            return "Email does not exist"
        return f"{self.fname}.{self.lname}@codewithharry.com"
    @printmail.setter
    def printmail(self,string):
        print("Setting ....")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]
    @printmail.deleter
    def printmail(self):
        # usually we dont delte in oops so we set its attributes to none 
        self.fname = None
        self.lname = None
# creating an object named skillf 
skillf = Employee("skill","f")
print(skillf.printmail)
# object intorospection is a process of obtaining all the infromation on a abject 
# determining the type of object 
print(type(skillf)) 
print(type("This is a string "))
# id is basically a unique id give to each object created 
print(id("This is a string "))
print(id("This is a stringa "))
# dir basically gives away everything that is consiting of the object 
o = "hello"
print(dir(o))
print(dir(skillf))
# inspect module 
import inspect
inspect.getmembers(skillf)