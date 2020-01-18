print(2+10 * 2+2)
mystring = 'abcdefg'
print('String = ' + mystring[1])
print('String[4:] = ' + mystring[4:])
print('String[:3] = ' + mystring[:3])
print('String[2:3] = ' + mystring[2:3])
print('Every 2 Character[::2] = ' + mystring[::2]) # Every 2 Character

mystring = 'Hello World'
print('String = ' + mystring[1])
print('string.split() = ')
print(mystring.split() )

print('"Insert another string here: {}".format("Insert me!") => ' + "Insert another string here: {}".format("Insert me!"))

print('"Item One: {y} Item Two: {x}".format(x = "dog", y="cat") => ' + "Item One: {y} Item Two: {x}".format(x = "dog", y="cat"))

# Lists

mylist = ['a','b','c','d','e']
print('Array = ' + "['a','b','c','d','e']")
print("Item One: array[-1] => " + mylist[-1])
mylist.extend(['f','g','h'])
mylist.append([1,2,3])
print("after extend and append => ")
print(mylist)

# List Comprehension
print('matrix = ' + "[[1,2,3],[4,5,6],[7,8,9]]")
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print('[row[0] for row in matrix] =>')
print(first_col)

#Dictionaries
print(">>Dictionaries")
my_stuff = {"key1": "value1", 'key2': 'value2'}
print(my_stuff)
my_stuff['key3'] = {'123':[1,2,'grabMe']}
print(my_stuff)
print(my_stuff['key3']['123'][2])

#Sets
print('Sets -- Unique')
xSets = set()
xSets.add(1)
xSets.add(2)
xSets.add(3)
xSets.add(4)
xSets.add(4)
xSets.add(4)
print(xSets)
