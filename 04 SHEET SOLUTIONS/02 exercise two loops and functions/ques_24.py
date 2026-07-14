# Count how many times each character appears in a string (dictionary + loop).

st = "kaizoku ou ni ore wa naru"
characters = list(st)
print(characters)
alphabets = {}
for ch in characters:
    if ch not in alphabets:
        alphabets[ch] = 1
    else:
        alphabets[ch] += 1
print(alphabets)





