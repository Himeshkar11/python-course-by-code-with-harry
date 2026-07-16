# i = 0
#
# # while (i<45):
# #     print(i+1)
# #     i = i+1
#
# while(True):
#     if i+1<5:
#         i = i+1
#         continue
#     print(i+1,end=" ")
#     if (i==44):
#         break #stop the loop
#     i = i + 1
# while(True) :
#     inp = int(input("Enter a Number"))
#     if inp >100:
#         print("Congrats you have enterd a number greater than 100")
#         break
#     else:
#         continue
# # revision material loading !
# emulation of while loop  ie irrespective of the condton the loop will continue and we describe condition inside it
i = 0
while True:
    print(i)
    i+=1
    if i%100 == 0:
        break
    else:
        print("the number is ",i)
# in this concpt is that it is a infinite loops which breaks as soon as the conditon inside it is fullfilled