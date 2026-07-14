#  12. Temperature Check
#  Write a program that takes a temperature in Celsius and prints whether
# it's "freezing" (below 0,
#  "cold" 015,
# "moderate" 16 to 25, or
# "hot" (above 25.
temperature_Celsius = int(input("Please enter the temperature in Celsius  ",))

if temperature_Celsius <0:
    print("the temperature in you are is now Freezing")
elif 0<=temperature_Celsius<=15:
    print("the temperature in you are is now Cold")
elif 16<=temperature_Celsius<=25:
    print("the temperature in you are is now Moderate")
else:
    print("the temperature in you are is now Hot")
    
    
    