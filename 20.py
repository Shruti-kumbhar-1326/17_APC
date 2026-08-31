# Open the file in read mode
file = open("transactions.txt", "r")

# Read all records
records = file.readlines()

# Close the file
file.close()

# Initialize variables
total_deposits = 0
total_withdrawals = 0
largest_transaction = 0
largest_type = ""

# Process each transaction
for record in records[1:]:
    transaction_type, amount = record.strip().split(",")

    amount = float(amount)

    # Calculate deposits
    if transaction_type.lower() == "deposit":
        total_deposits += amount

    # Calculate withdrawals
    elif transaction_type.lower() == "withdrawal":
        total_withdrawals += amount

    # Find largest transaction
    if amount > largest_transaction:
        largest_transaction = amount
        largest_type = transaction_type

# Calculate final balance
final_balance = total_deposits - total_withdrawals

# Display results
print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)
print("Transaction Type:", largest_type)