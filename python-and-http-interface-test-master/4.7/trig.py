#很显然，双重循环的效率会更低
import time
high = int(input("请输入塔高"))
first = time.time()
for line in range(1,high):
    for col in range(1,high-line+1):
        print(" ",end="")
    for star in range(1,line*2):
        print("*",end="")
    print("")
last = time.time()
print(last-first)



