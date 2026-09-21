class Shape:
    def display(self):
        print("Shape")


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self, length, breadth):
        return length * breadth


class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height


c = Circle()
r = Rectangle()
t = Triangle()

c.display()
print("Circle Area =", c.area(5))

r.display()
print("Rectangle Area =", r.area(10, 5))

t.display()
print("Triangle Area =", t.area(10, 6))