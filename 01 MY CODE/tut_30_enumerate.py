# enumarate is a function which directly gets the index of iterable objects

li = ["Honda","Suzuki","Tokyo","Kyoto"]
for index,name in enumerate(li):
    if index%2==0:
        print(f"{index} is the best for {name}")
# we can also cahnge the index as per our request
liu = ["luffy","naruto","Ichigo","goku"]
print("the best anime protagainsts are")
for index,name in enumerate(liu,start=1):
    print(f" \n {index} {name}")
