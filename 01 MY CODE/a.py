list_new = [1,2,2,3,2]
list_blank =[]

for i in list_new:
    if i ==2:
        continue
    else:
        list_blank.append(i)
    
print(list_blank)