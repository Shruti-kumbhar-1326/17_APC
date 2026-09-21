class FoodOrder:
    def __init__(self, order_id, name, food, quantity, price):
        self.order_id = order_id
        self.name = name
        self.food = food
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        return total + tax

    def __del__(self):
        print("Order Completed")


o = FoodOrder(101, "Rahul", "Pizza", 2, 200)

print("Order ID =", o.order_id)
print("Customer =", o.name)
print("Food =", o.food)
print("Quantity =", o.quantity)
print("Price =", o.price)
print("Total Bill =", o.total_bill())

del o