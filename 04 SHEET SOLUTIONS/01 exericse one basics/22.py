# 22. Password Strength Checker
#  Write a program that evaluates password strength based on:
#  Length (minimum 8 characters)
#  Contains uppercase and lowercase letters
#  Contains at least one digit
#  Contains at least one special character
#  Rate as "Weak", "Medium", or "Strong"
password_input=input("Enter your password here:",)

length_ok =   len(password_input) >= 8

