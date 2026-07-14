#  16. Login System
#  Create a simple login system that checks if the entered
# username is "admin"
# and password is"python123".
# Print appropriate success or failure message

a = "admin"
b = "python123"

print("Welcome to the portal please do the following")
username_input = input("please enter your username here :",)
if username_input == a :
    print ("Success you have Succesfully entered the username now enter the password below ")
else :
    print("OOPS! You have entered user name wrong\n please try again ")
password_input= input("Please enter your password here : ",)
if password_input == b :
    print ("Success you have Succesfully entered the password \n now you can login to your account")
else :
    print("OOPS! You have entered \n password wrong please try again ")
    
