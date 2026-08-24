#28.	Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.
products = {}


def add_product(name, price, quantity):
    products[name] = [price, quantity]
    print("Product added successfully.")


def remove_product(name):
    if name in products:
        del products[name]
        print("Product removed successfully.")
    else:
        print("Product not found.")


def calculate_subtotal():
    subtotal = 0

    for price, quantity in products.values():
        subtotal += price * quantity

    return subtotal


def apply_coupon(subtotal, coupon):
    if coupon == "SAVE10":
        discount = subtotal * 0.10
    elif coupon == "SAVE20":
        discount = subtotal * 0.20
    else:
        discount = 0

    return discount


def calculate_gst(amount):
    return amount * 0.18       # 18% GST


def generate_invoice(coupon):
    subtotal = calculate_subtotal()

    discount = apply_coupon(subtotal, coupon)

    amount_after_discount = subtotal - discount

    gst = calculate_gst(amount_after_discount)

    final_amount = amount_after_discount + gst

    print("\n----- FINAL INVOICE -----")

    for name, (price, quantity) in products.items():
        print(name, "₹", price, "x", quantity,
              "=", price * quantity)

    print("------------------------")
    print("Subtotal        = ₹", subtotal)
    print("Coupon Discount = ₹", discount)
    print("GST (18%)       = ₹", gst)
    print("Final Amount    = ₹", final_amount)


# Main program
add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
add_product("Keyboard", 2000, 1)

# Remove a product if required
# remove_product("Mouse")

coupon = input("Enter coupon code (SAVE10/SAVE20/None): ")

generate_invoice(coupon)