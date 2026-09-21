class Shape:
    def area(self):
        print("Area of shape")


class Circle(Shape):
    def area(self):
        radius = 5
        print("Area of Circle =", 3.14 * radius * radius)


class Rectangle(Shape):
    def area(self):
        length = 10
        breadth = 5
        print("Area of Rectangle =", length * breadth)


class Triangle(Shape):
    def area(self):
        base = 8
        height = 6
        print("Area of Triangle =", 0.5 * base * height)


# Create objects
shapes = [Circle(), Rectangle(), Triangle()]

# Runtime Polymorphism
for shape in shapes:
    shape.area()