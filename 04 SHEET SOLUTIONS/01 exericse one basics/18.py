#  18. BMI Calculator with Categories Calculate BMI 
# (weight in kg / (height in meters)²) and categorize it:
# Underweight 18.5, Normal 18.5 to 24.9,
# Overweight 25 to 29.9, Obese ≥ 30.

a = int(input("Enter your weight(in kg) here :"))
b = int(input("Enter your height here(cm) :"))
e = b/100
c = e**2
d = a/c
print("Your BMI is ",d)
if d < 18.5 :
    print("You are under weight") 
elif 18.5<= d <=24.9:
    print("You are normal")
elif 25<= d <=29.9:
    print("You are over weight")
else:
    print("You are obese")
