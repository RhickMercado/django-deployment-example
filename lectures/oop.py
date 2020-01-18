
print('>> My List')
mylist = [1,2,3]
mylist.append(4)
print(mylist)

class Dog():
    species = "Mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

myDog = Dog(breed = "Lab", name = 'Sammy')
otherDog = Dog(breed="huskie", name = 'husk')

print('>> Class Dog')
print(type(myDog))
print(otherDog.breed)
print(myDog.breed)
print(myDog.species)

print('>>> Circle')
class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(3)
print('Radius:', myc.radius)
print('Area:', myc.area())

myc.radius = 100
print('Radius:', myc.radius)
print('Area:', myc.area())

myc.set_radius(10)
print('Radius:', myc.radius)
print('Area:', myc.area())
