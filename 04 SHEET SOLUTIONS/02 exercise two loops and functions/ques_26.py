# Remove all punctuation from a string without regex or replace.
str = "this is a string, and this will be a string."
ch = list(str)

punctuatuion = [" ",",","."]
final = []
for i in ch:
    if i in punctuatuion:
        continue
    else:
        final.append(i)
s = "".join(final)
print(s)


