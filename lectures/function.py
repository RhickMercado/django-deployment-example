def my_func(param1='default'):
    """
    This is the DocString
    """
    print("my first python function! {}".format(param1))
    return 'Hello'

print(my_func('Rhick'))

print(type(my_func('Rhick')))

print("Lambda Expression")

# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0
evens = filter(even_bool, mylist)
print(list(evens))

print(filter(lambda num:num%2 == 0, mylist))

def arrayCheck(nums):
    a = True
    for i in [1,2,3]:
        if i not in nums:
            a = False
    return a

print(arrayCheck([1,1,2,3,1]))
print(arrayCheck([1,1,2,4,1]))
print(arrayCheck([1,1,2,1,2,3]))

def stringBits(str):
    return str[::2]

print(stringBits('Hello')) #Hlo
print(stringBits('Hi')) #H
print(stringBits('Heeololeo')) #Hello

def end_other(str1, str2):
    # return b.endswith(a) or a.endswith(b)
    return str1[-(len(str2)):].lower() == str2.lower() or str2[-(len(str1)):].lower() == str1.lower()

print('>>>end_other')
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

def doubleChar(str):
    s = ''
    for i in str:
        s = s + i*2
    return s

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13,14,17,18,19]: #range(13,20):
        return 0
    return n

print('>>> no_teen_sum')
print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))

def count_evens(nums):
    c = 0
    for i in nums:
        if i % 2 == 0:
            c = c + 1
    return c

print('>>> count_evens')
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
