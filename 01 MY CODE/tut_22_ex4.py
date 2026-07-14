print("Hello welcome to the Astrologer game !!")
n = int(input("Enter the number of rows you want to print:"))
choice = bool(int(input("Enter 1 for correct pattern \n 0 for reverse pattern")))
if choice:
    print("Correct pattern")
    for i in range(n+1):
        print(("*"*i).center(n-i))
else:
    print("Incorrect pattern")

    for i in range(n+1):
        j = (n) - i
        print(("*"*j).center(n-i))

