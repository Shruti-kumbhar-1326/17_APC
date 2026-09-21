class Camera:
    def take_photo(self):
        print("Taking photograph...")


class Phone:
    def make_call(self):
        print("Making a phone call...")


class Smartphone(Camera, Phone):
    def use_smartphone(self):
        print("Smartphone is ready")


# Create object
s = Smartphone()

s.use_smartphone()
s.take_photo()
s.make_call()