#18.	Create a shopping cart using a list.Perform:
#•	Add item 
#•	Search item 
#•	Display cart 
#•	Count total items
cart = []

# Add items
n = int(input("How many items do you want to add? "))

for i in range(n):
    item = input("Enter item: ")
    cart.append(item)

# Search item
search = input("Enter item to search: ")

if search in cart:
    print("Item found in cart.")
else:
    print("Item not found in cart.")

# Display cart
print("Shopping Cart:", cart)

# Count total items
print("Total items:", len(cart))