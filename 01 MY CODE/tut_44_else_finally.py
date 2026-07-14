# WE ALREADY KNOW FILE HANDLING
f1 = open("himi.txt") 


try:
    f = open("dojes.txt")
except Exception as e :
    print(e)
else: 
    print("This will run only if except does not ")
# used in code cleanup
finally :
    print("Run this anyway")
    # f.close()
    f1.close()
print("Important sstuff ")

