class ShoppingCart:
    def __init__(self, name, cart_id):
        self.name = name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, product, price):
        self.products.append([product, price])

    def remove_product(self, product):
        for p in self.products:
            if p[0] == product:
                self.products.remove(p)

    def total_bill(self):
        total = 0
        for p in self.products:
            total = total + p[1]
        return total

    def __del__(self):
        print("Shopping Cart Destroyed")


c = ShoppingCart("Rahul", 101)

c.add_product("Mobile", 20000)
c.add_product("Mouse", 500)

c.remove_product("Mouse")

print("Customer =", c.name)
print("Cart ID =", c.cart_id)
print("Total Bill =", c.total_bill())

del c