# setters gettters and property decorators 

# creating a class named employee 
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
# creating two objects of the Employee class 
Hindusthani_supporter = Employee("Hindusthani","Supporter")
nikhil_raj_pandey = Employee("nikhil","raj")
# printing the explain function of both the objects
print(Hindusthani_supporter.Explain())
print(nikhil_raj_pandey.Explain())
print(Hindusthani_supporter.printmail)

# if hindhusthani supporter wnat to change his name into us suppoerter 
Hindusthani_supporter.fname = "US"
print(Hindusthani_supporter.fname) # this will change 
print(Hindusthani_supporter.printmail) # but this will not change 
# the reason for this is the construtor ran at the run time and took the inital values 
# now we cant undo that and this is thed problem 
# to solve this problem there exists something called as setter
# after changing the email from constructor to creating a method the mail
# hindusthani supppoeter changed to us supporter 
# but we want to use the emial as an attribute  we use property decorator
# now what i want is to pass arguments inot email and that should change the fname and lname 
# for this we use setterss and getters 
Hindusthani_supporter.printmail= "this.that@gmail.com"
print(Hindusthani_supporter.fname)
print(Hindusthani_supporter.lname)
print(Hindusthani_supporter.printmail)
# to delete  the any attribulte we cannot directly write del object.attribute 
# we need to specifiy a deleter inside the class 
# del Hindusthani_supporter.printmail # will give an err 
del Hindusthani_supporter.printmail
print(Hindusthani_supporter.printmail)