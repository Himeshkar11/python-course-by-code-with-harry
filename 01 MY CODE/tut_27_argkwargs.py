# # # the neccesity of *args and **kwags
# # def func(a,b,c,d):
# #
# #      return print(a,b,c,d)
# #
# # func("himesh","Kyo ronin","Matsuda","Kino kaizoku","risa")
# # # if we add another person risa here we will get an error saying TypeError: func() takes 4 positional arguments but 5 were given
# # # so we use args for this type
# def func(*args):
#     print(type(args))
#     for i in args:
#          print(i)
# har =["himesh","Kyo ronin","Matsuda","Kino kaizoku","risa"]
# func(*har)
# # if we now update the list then also the new entry will be printed
# har.append("Maddie Slayer")
# func(*har)
# # this take the input and behaves like a tuple
# # now lets talk aabout kwargs these are same as args but they give dictionary as output
def func(**kwargs):
    for key, value in kwargs.items():
         print(f'{key} is shiriai of {value}')

dict = {"Kyoronin":"Risa","Kyoroninn":"tomoki","Himesh":"poly"}
func(**dict)
# note that always first use normal then args then kwargs inside a function bracket right
