class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand =", self.brand)
        print("Model =", self.model)
        print("Storage =", self.storage)
        print("Price =", self.price)

    def discount(self):
        return self.price - (self.price * 10 / 100)


m = MobilePhone("Samsung", "A15", "128GB", 20000)

m.display()
print("Price after discount =", m.discount())