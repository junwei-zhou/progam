#直接注入pycharm中路径是找不到的，有必要将其标志位source路径
from calculator import *

operator = input('''选择运算符:
1 is +
2 is -
3 is x
4 is ÷
输入你的选择（1/2/3/4）:
''')
if(int(operator)<1 or int(operator)>4):
    print("这不是一个合法的运算符")
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
if(operator == "1"):
    print(add(num1,num2))
if(operator == "2"):
    print(minus(num1,num2))
if(operator == "3"):
    print(multiply(num1,num2))
if(operator == "4"):
    print(divide(num1,num2))
