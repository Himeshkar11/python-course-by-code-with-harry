#genrally pro python programmers use if lese like this
a = int(input("Enter your number A",))
b = int(input("Enter your number B",))

if a>b:print("A B se bada hai bhai ")

print("B A se bada hai bhai") if a<b else print("A B se bada hai bhai ")

# match case statements
x = 40
match x :
    case 40:
        print("case is 40 ")
    case 147:
        print("case is 147 ")
    case _:
        print("this shit is confusing lol!")

