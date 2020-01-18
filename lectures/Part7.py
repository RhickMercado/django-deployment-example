if 1<2:
  print('First Block')
  if 30 < 3:
      print('Second Block')
  elif 3 == 3:
      print('elif run')

# for Loops
seq = [1,2,3,4,5,6]
for item in seq:
    print(item)

d = {"Sam": 1,"Frank": 2, "Dan": 3}
for k in d:
    print(k)
    print(d[k])

print('Tuple for loop')
mypairs = [(1,2),(3,4),(5,6)]
for tup1, tup2 in mypairs:
    print(tup2)
    print(tup1)

print('While loop')
i = 1
while i<5:
    print("i is: {}".format(i))
    i = i + 1

print("range(0, 5) => {}".format(range(0, 5)))

print("range(0, 21, 2) => {}".format(range(0, 21, 2)))

print("range(3, 21, 3) => {}".format(range(3, 21, 3)))

print("[num**2 for num in [1,2,3,4]] => {}".format([num**2 for num in [1,2,3,4]]))
