s = set()
# print(type(s))

set_one = set([1,2,3,4])
print(set_one)

set_one.pop()
print(set_one)

set_one.pop()
print(set_one)
set_one.pop()
print(set_one)
set_one.pop()
print(set_one)

sets = set(["Risa", "Madiiesalyer","kyoronin","yanagi"])
sets.add("Himesh")
sets.add("Senpai")

# print(sets)

setss = set(["Risa","Kino Kaizoku","kyoronin","luffy","shanks"])
print(sets.intersection(setss))
print(sets.union(setss))

def integerinput (x) :
    x = int(input("Enter a number: "))
    print(x)
