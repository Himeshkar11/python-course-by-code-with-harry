# Print a multiplication table 1 10)
# using nested loops.
factor = [1,2,3,4,5,6,7,8,9,10]
table = [1,2,3,4,5,6,7,8,9,10]
for i in factor:
    print(f"table of {i}")
    for j in table:
        print(i*j)
        