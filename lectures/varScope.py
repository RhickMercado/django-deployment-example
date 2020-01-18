x = 25

def my_func():
    x = 50
    return x
#
# print(x)
# print(my_func())
# print(x)

#LOCAL

# print(lambda x: x**2, [10])

# Enclossinf function locals
name = 'This is a global name!'

def greet():
    name = "sammy"

    def hello():
        print("hello " + name)

    hello()

greet()
print(name)


x = 50
y = 100
def func(x):
    print('x is:', x)
    global y
    y = 2000
    x = 1000
    print('local x changed to: ', x)

func(x)
print(x)
print('Global y', y)
