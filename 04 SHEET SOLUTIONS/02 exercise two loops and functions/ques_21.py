# Function to return only unique elements from
# a list (no duplicates, using loops).

li = [1,2,3,1,4,2,53,12,1,2,3,4]
og = []
for i in li:
    if i not in og:
        og.append(i)
    else:
            continue

print(og)