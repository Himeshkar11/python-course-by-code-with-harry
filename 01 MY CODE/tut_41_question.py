# question from harri bai : 
# take the number of elements input and using for loop take input of all those 
# ask the user which comprehension to be made 
# create the comprehension for the user 
name = input("Give a name to the things you want to add ")
n = int(input(f"Enter the number of {name} here:-"))
l = []
for i in range(n):
    l.append(input(f"Enter the {name} {i+1}"))
print(f"choose the type of comprehension that you want to create for {name}")
print("1.listcomprehension \n 2. dictionarycomprehension \n 3. set comprehension")
choice = int(input())
def listcomprehension(li):
    return [i for i in li]
     
def dictcomprehension(li):
    return {i: value for i, value in enumerate(li)}

def setcomprehension(sett):
    return {i for i in sett}
    
if choice==1:
    answer = listcomprehension(l)
    print(answer)
elif choice ==2:
    answer = dictcomprehension(l,n)
    print(answer)
elif choice ==3:
    answer = setcomprehension(l)
    print(answer)
else:
    print("Some error ! retry ")
    