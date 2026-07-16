#Write a function to count vowels in a string
from numpy.ma.core import count

st = "this is a string"
vowel = ["a","e","i","o","u"]
total = list(st)
counting = 0
for j in total:
    if j in vowel:
        counting+=1
print(counting)



