# for loop ke saath else tab hi chalega when for loop normally end ho ie without using any break statement 
# else ke andhar tab jaayega when for loop normally end ho
# # runs properly  
items =["idly","dosa","sambar"]
for item in items:
    print(item)
    
else: 
    print("This for loop ended successfully")
# with break statement 
items =["idly","dosa","sambar"]
for item in items:
    print(item)
    break
else: 
    print("This for loop ended successfully")


# kis tarah use kar sate hai
# used in searching or finding objects 
items =["idly","dosa","sambar"]
for item in items:
    if item =="dosa":
        break
    
else: 
    print("your item was not found")