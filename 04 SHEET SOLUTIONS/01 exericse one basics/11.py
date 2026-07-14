#   11. Age Category
#  Write a program that takes a person's age and prints whether they are a "child" (under 18,
#  "adult" 1864, or "senior" 65 and above)
age_person = int(input("Please enter your age ",))

if age_person <18 :
    print("You are still a Minor")
elif 18 <=age_person <=64 :
    print("You are an Adult ")
else:
    print("You are a Senior citizen ")
    