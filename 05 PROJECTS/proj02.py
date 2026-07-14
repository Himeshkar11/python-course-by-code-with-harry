# project 2 Richter Scale:
pre = [1,5.0,9.1,9.2,9.5]
print("Richther              joules                tnt ")
for i in pre:
    E = 10**((1.5*i)+4.8)
    tnt = (1)/(4.184*10**9)
    print(f"{i}                {E}                   {E*tnt}")
a = float(input("Please enter a Richter scale value:"))
print(f"Richter scale value : {a}")
print(f"Equivalence in Joules : {10**((1.5*a)+4.8)}")
print(f"Equivalece int tons of TNT : {(a)/(4.184*10**9)}")