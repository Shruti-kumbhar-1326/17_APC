class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof")


class Cat(Animal):
    def sound(self):
        print(self.name, "says Meow")


class Cow(Animal):
    def sound(self):
        print(self.name, "says Moo")


# Create objects
d = Dog("Tommy")
c = Cat("Kitty")
w = Cow("Gauri")

d.eat()
d.sound()

c.eat()
c.sound()

w.eat()
w.sound()