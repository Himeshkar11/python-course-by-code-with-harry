# # f = open("himi.txt","rt") # this will opwen the fie
# #  # content = f.read() # the number enterd in this () will make sure that it will print upto that index only
# # # print(content)
# # # content = f.read(4)
# # # print(content)
# # # content = f.read(4) # THIS WILL PRINT THE CHARCTERS AFTER THE ABOVE SELECTED ONES
# # # print(content)
# # # for line in f:
# # #     print(line)
# #
# # contents = f.readline() # this will completely read the line by line
# # print(contents)
# # contents = f.readline()
# # print(contents)
# # contents = f.readline()
# # print(contents)
# #
# # content = f.readlines() # this will convert all the lines into list
# # print(content)
# #
# # f.close()# we have to close every file we opened
# #
# # f = open("himi.txt","a")
# # a = f.write("My laptop name is HP Victus\n ") # this will erase all the data and will rewrite the content in it
# # print(a) # this will tell how many chracters did we printed in that txt
# # f.close()
# # f = open("sonti.txt","w")# if there is no file with that name in the pc it will make the file with that name
# #
# # f.write("SOnti alias sonu santosh is a baka ototouto")
# #
# # # r+ is a mode which is used for both write and read
# # f.close()
# #
# f = open("sonti.txt","r+")
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.seek(0))
# f.write("Bye!")
# # print(f.read())
# f.close()
# with open ("sonti.txt","r+") as f:
#     a=f.read(4)
#     print(a)
    # this is like the combination of both open and close tags
f = open(" sasikar-food.txt","r+")
print(f.readline())

