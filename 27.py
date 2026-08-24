#27.	Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.
def consultation_charges(consultation_fee):
    return consultation_fee


def laboratory_charges(lab_fees):
    return sum(lab_fees)


def medicine_charges(medicine_fees):
    return sum(medicine_fees)


def room_charges(room_charge, days):
    return room_charge * days


def calculate_discount(total, category):
    if category.lower() == "senior citizen":
        return total * 0.20       # 20% discount
    elif category.lower() == "student":
        return total * 0.10       # 10% discount
    elif category.lower() == "regular":
        return 0
    else:
        return 0


def final_bill(consultation, lab, medicine, room, category):
    subtotal = consultation + lab + medicine + room
    discount = calculate_discount(subtotal, category)
    bill = subtotal - discount

    return subtotal, discount, bill


# Input
consultation = float(input("Enter consultation charges: "))

lab_count = int(input("Enter number of laboratory tests: "))
lab_fees = []

for i in range(lab_count):
    fee = float(input("Enter laboratory charge: "))
    lab_fees.append(fee)

medicine_count = int(input("Enter number of medicines: "))
medicine_fees = []

for i in range(medicine_count):
    fee = float(input("Enter medicine charge: "))
    medicine_fees.append(fee)

room_charge = float(input("Enter room charge per day: "))
days = int(input("Enter number of days: "))

category = input("Enter patient category (Regular/Student/Senior Citizen): ")


# Calculate charges
consultation = consultation_charges(consultation)
lab = laboratory_charges(lab_fees)
medicine = medicine_charges(medicine_fees)
room = room_charges(room_charge, days)

subtotal, discount, bill = final_bill(
    consultation, lab, medicine, room, category
)


# Display bill
print("\n----- HOSPITAL BILL -----")
print("Consultation Charges = ₹", consultation)
print("Laboratory Charges   = ₹", lab)
print("Medicine Charges     = ₹", medicine)
print("Room Charges         = ₹", room)
print("Subtotal             = ₹", subtotal)
print("Discount             = ₹", discount)
print("Final Bill           = ₹", bill)