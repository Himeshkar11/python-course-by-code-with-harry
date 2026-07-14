# Loop 1 20, skip multiples of 3, break at 15
for i in range(21):
    if i == 15:
        break
    elif i%3 == 0:
        continue
