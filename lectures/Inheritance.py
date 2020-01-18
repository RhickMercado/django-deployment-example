#Inheritance

class Animal():
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof")


# mya = Animal()
# mya.whoAmI()
# mya.eat()

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()

#Special Methods

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}. Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages


mylist = [1,2,3]
print(mylist)
len([1,2,3])

b = Book("Python", "Jose", 200)
print(b)
print(len(b))
