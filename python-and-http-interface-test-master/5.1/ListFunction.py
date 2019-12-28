def foo1():
    print("this is foo1!")
def foo2():
    print("this is foo2!")
listFun = [foo1,foo2]
#程序的入口
for function in listFun:
    function()

def foo():
    print("foo")
#程序的二次入口
function = foo
function()