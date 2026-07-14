# def searcher():
#     import time 
#     # some 4 sec time onsuimg task 
#     book = "THIS IS A BOOK AFTER YOU LLWLDNLSNDL"
#     time.sleep(4)
    
#     while True:
#         text =(yield) # meaning the given func will become an coroutine 
#         if text in book:
#             print("TExt is in book")
#         else:
#             print("text is not in the book")
            
# search = searcher()
# print("SEarch started ...")
# next(search)
# search.send("Himesh")
# print("next method run ..")
# input("press any key")
# search.send("AFTER YOU")
# # input("press any key")
# # search.send("AFTER YOU")
# # input("press any key")
# # search.send("AFTER YOU")
# # input("press any key")
# # search.send("AFTER YOU")
# search.close()
# challenge question 
def names():
    import time 
    # some 4 sec time onsuimg task 
    book = "Himesh Santosh Luffy Zoro Sanji OKarun Momo Kyoronin"
    time.sleep(4)
    
    while True:
        text =(yield) # meaning the given func will become an coroutine 
        if text in book:
            print("TExt is in book")
        else:
            print("text is not in the book")
anime = names()
i = input("Enter a name ")
print("SEarch started ...")
next(anime)
anime.send(i)
