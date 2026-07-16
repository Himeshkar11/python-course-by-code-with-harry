#  19. Nested Conditions - Scholarship Eligibility
#  Write a program that determines scholarship eligibility based on:
#  GPA must be ≥ 3.5
#  Family income must be < $50,000
#  Student must be enrolled full-time (boolean)
#  Print detailed eligibility status with reasons.

cgpa_input = float(input("Please enter your CGPA here :"))
family_income_input= int(input("Please enter our family income(in dollars)"))


preferences_input=bool(int(input("please enter your preferences \n for enrollment period fulltime select 1 \n for enrollment period not fulltime select 0 ")))
cgpa_ok = cgpa_input >= 3.5
income_ok = family_income_input < 50000
fulltime_ok = preferences_input

if  cgpa_ok:
    print("YES! with the cgpa of ",cgpa_input,"you can enter the scholarship \n now continue the process below")
else:
    print("WE are sorry ! you do not meet the criteria of cgpa under this scholarship")

if income_ok:
    print("YES! with the family income of ",family_income_input,"you can enter the scholarship \n now continue the process below")
else:
    print("WE are sorry ! you do not meet the criteria of family income  under this scholarship")

if fulltime_ok == True :
    print("Yes you are eligible for this scholarship")
elif fulltime_ok == False :
    print("We are sorry to inform you that only full time courses are available please try again ")

if fulltime_ok and  income_ok<=50000 and fulltime_ok :
    print("YOHOHO! you are selected for this scholarship")
else :
    print("WE are sorry ! you do not meet the criteria of  this scholarship")
