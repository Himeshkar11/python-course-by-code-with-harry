# Write a function that calculates the 
# sum of the first n numbers using a loop

def natural_sum(n):
    total = 0
    for i in range(n+1):
        total = total + i 
    print(total)
        

natural_sum(5)