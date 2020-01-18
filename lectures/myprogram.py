import myModule
myModule.func_in_module()

s = "GLOBAL VARIABLE"

def func():
    s = 50
    print("Func set s", s)
    print(locals())
    print(globals())
    print(globals()["s"])
    return 1

def func2():
    global s
    s = 50
    print("Func2 set s", s)
    return 1

def hello(name="Jose"):
    return "Hello " + name

print('Global s before:', s)
func()
print('Global s after func:',s)
func2()
print('Global s after func2:', s)

print('func Hello ')
print(hello())

print('mynewgreet =  Hello() ')
mynewgreet = hello

print(mynewgreet())
