import time
initalize = time.time()
i = 0
while i<45:
    print(i)
    time.sleep(1)
    i = i + 1

now = (time.time()-initalize)
end =print(f"while loop ran for {now} seconds")
initalize2 = time.time()



for i in range(45):
    print(i)
now2 = (time.time()-initalize2)
print(f"for loop ran for {now2} seconds")

# that way we can clealy track time taken between any line of code

localtime = time.localtime(time.time())

print(localtime)



