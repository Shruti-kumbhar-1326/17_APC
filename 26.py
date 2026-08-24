#26.	Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.
def calculate_energy_charge(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + ((units - 100) * 7)
    else:
        return (100 * 5) + (100 * 7) + ((units - 200) * 10)


def calculate_fixed_charge():
    return 100


def calculate_tax(amount):
    return amount * 0.05       # 5% tax


def calculate_discount(amount):
    if amount >= 2000:
        return amount * 0.10   # 10% discount
    else:
        return 0


def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)
    fixed_charge = calculate_fixed_charge()

    subtotal = energy_charge + fixed_charge

    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount

    tax = calculate_tax(taxable_amount)

    final_bill = taxable_amount + tax

    return energy_charge, fixed_charge, discount, tax, final_bill


# Main program
units = int(input("Enter electricity units consumed: "))

energy, fixed, discount, tax, total = calculate_bill(units)

print("\n----- ELECTRICITY BILL -----")
print("Energy Charge = ₹", energy)
print("Fixed Charge  = ₹", fixed)
print("Discount      = ₹", discount)
print("Tax           = ₹", tax)
print("Final Bill    = ₹", total)