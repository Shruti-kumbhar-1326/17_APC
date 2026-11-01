from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

    def stop(self):
        print("Bike is stopping")


class Bus(Vehicle):
    def start(self):
        print("Bus is starting")

    def stop(self):
        print("Bus is stopping")


# Create objects
car = Car()
bike = Bike()
bus = Bus()

# Call methods
car.start()
car.stop()

bike.start()
bike.stop()

bus.start()
bus.stop()