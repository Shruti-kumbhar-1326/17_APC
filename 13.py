class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice(Printer, Scanner):
    def multifunction(self):
        print("Multifunction Device")


# Create object
m = MultifunctionDevice()

m.print_document()
m.scan_document()