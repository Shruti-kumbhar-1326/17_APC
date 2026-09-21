class ElectricityBill:
    def __init__(self, number, name, units):
        self.number = number
        self.name = name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5
        elif self.units <= 200:
            bill = 100 * 5 + (self.units - 100) * 7
        else:
            bill = 100 * 5 + 100 * 7 + (self.units - 200) * 10

        return bill


e = ElectricityBill(101, "Rahul", 250)

print("Consumer Number =", e.number)
print("Consumer Name =", e.name)
print("Units =", e.units)
print("Electricity Bill =", e.calculate_bill())