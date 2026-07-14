# # there is a shop which gives
# # 10 percent discount for shopping more than 5k
# # 20 percent for shooping more than 10k
# # 30 perecent for shopping more than 20k
# while True :
#     rawcost = int(input("Enter the raw cost: "))
#
#     if rawcost < 5000:
#         print("you shopped for  5000 only , \n discount not available.")
#     elif 5000<= rawcost < 10000:
#         discount_1 = int((rawcost)/10)
#         print("you shopped for",rawcost,"which is greater than or equal to  10000  , \n discount is  available.")
#         print("Your discount was 10 percent so please pay " , (rawcost) - (discount_1))
#     elif 10000 <= rawcost < 20000:
#         discount_1 = int((rawcost) / 20)
#         print(f"you shopped for {rawcost}   which is more than 20000, \n discount is  available.")
#         print("Your discount was 20 percent so please pay ", (rawcost) - (discount_2))
#     elif 20000<= rawcost:
#         discount_3 = int((rawcost)/30)
#         print(f"you shopped for{rawcost}   which is more than or equal to 10000  , \n discount is  available.")
#         print("Your discount was 30 percent so please pay " , (rawcost) - (discount_3))
#
#
#
#
#
# Q - 1.a
# Initialization:
x = None
# Access
print(x)
# Update : Variable can be reassigned to another value x = 10
# Insert/remove : Not possible because it’s not a collection
a = 10

