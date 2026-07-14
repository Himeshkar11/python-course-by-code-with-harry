# DICTIONARY IS A SET OF KEYS AND ITEMS

D1 = {}
# print(D1)

dict = {"Himesh" : "dosa",
        "ramesh" : "idly",
        "yukiko" : "sushi",
        "Subaru": {"m":"emilia", "a" : "rem" , "nt" : "ferris"}}
print(dict)

print(dict["Subaru"])

dict["sonti"] = "Ice cream"
dict["Appi"] = "appadam"
dict[456]   = " seong- gi hun "

print(dict)

print(dict[456])

# del  is a function which deletes that entry entirely

del dict["Appi"]

print(dict)

d3 = dict.copy()
del d3["sonti"]
print(d3)

dict.update({"Luffy" : 'meat'} )

print((dict))

