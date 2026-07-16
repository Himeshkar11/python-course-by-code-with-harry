grocery =["toilet cleaner","vim bar", "deodorant","tomato" "Lollipop",56]
print(grocery[2])
#when i print grocery[5] it will show mw an error because there ios no elementary at index of 5
numbers = [2,7,9,11,3]
numbers.sort()
numbers.reverse()

print(numbers)

print(numbers[::])

print(numbers[::-1])#this reverse the list ans in sting also it reverses the string also

numbers.append(456)
numbers.append(222)
numbers.append(333)
numbers.append(147)
numbers.append(289)
print(numbers)
numbers.insert(0,456)
numbers.remove(222)
numbers.pop(5)

print(numbers)

# now we start  tuples
 #so basically we represent tuples with parenthesis brackets and they are immutable  ie not change able where as lists are mutable ie changeable

tp = (1,89,456)

print(tp)

#tp[1] = 526
#print(tp)
# comes a type error because tuples are immutable
''' 
    tp[1] = 526
    ~~^^^
TypeError: 'tuple' object does not support item assignment'''

# suppose we give a = 1 and b = 8 now we want them to interchange their values then normally we do like this
a = 1
b = 8
#temp = a
#a = b
#b = temp
#print(a,b)

#in python we can also do like this
a,b = b,a
print(a,b)
