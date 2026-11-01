#9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
city = ["kagal", "kolhapur", "sulkud", "tasgaon", "pune"]

name = input("Enter a city name to check: ")

if name in city:
    print("City exists in the list.")
else:
    print("City does not exist in the list.")   