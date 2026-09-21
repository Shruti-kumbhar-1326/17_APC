class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand =", self.brand)


class Car(Vehicle):
    def __init__(self, brand, price):
        super().__init__(brand)
        self.price = price


class Bike(Vehicle):
    def __init__(self, brand, mileage):
        super().__init__(brand)
        self.mileage = mileage


class SportsCar(Car):
    def speed(self):
        print("Sports Car Speed = 250 km/h")


class ElectricBike(Bike):
    def battery(self):
        print("Battery = 5 kWh")


s = SportsCar("BMW", 5000000)
e = ElectricBike("Ola", 120)

s.display()
print("Price =", s.price)
s.speed()

print()

e.display()
print("Mileage =", e.mileage)
e.battery()