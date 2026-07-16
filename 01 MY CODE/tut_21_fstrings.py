letter = "hello my name is {} and i am from {}"
name = input("What is your name?: ")
country = input("Enter your country name :")

print(letter.format(name,country))

# but his is a tiring process so we use f strings here
# f string means we can keep variables in a string
print(f"hello my name is {name} and i am from {country}")

print(f"hello my name is {{name}}and i am from {{country}}") # here ehat hhappens is that we willl driectly see the curly brackets

