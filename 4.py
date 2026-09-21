class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says Moo")


class Lion(Animal):
    def sound(self):
        print("Lion says Roar")


# Create objects
animals = [Dog(), Cat(), Cow(), Lion()]

# Runtime Polymorphism
for animal in animals:
    animal.sound()