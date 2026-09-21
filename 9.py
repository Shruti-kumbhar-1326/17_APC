class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches

        # Convert extra inches into feet
        feet = feet + inches // 12
        inches = inches % 12

        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


# Create two objects
d1 = Distance(5, 8)
d2 = Distance(3, 7)

# Add two distances
d3 = d1 + d2

print("First Distance:")
d1.display()

print("Second Distance:")
d2.display()

print("Total Distance:")
d3.display()