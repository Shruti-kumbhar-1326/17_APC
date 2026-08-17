#4.	Create a tuple of colors. Check whether a given color exists in the tuple
colors = ("red", "blue", "green", "yellow", "pink")

color = input("Enter a color to search: ")

if color in colors:
    print("Color exists in the tuple.")
else:
    print("Color does not exist in the tuple.")