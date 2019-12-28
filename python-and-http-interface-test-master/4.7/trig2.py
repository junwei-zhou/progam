import time
high = int(input("请输入塔高"))
first = time.time()
for line in range(1,high):
    print(" "*(high-line)+"*"*(line*2-1))
last = time.time()
print(last-first)