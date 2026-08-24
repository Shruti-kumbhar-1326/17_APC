#21.	Create a function that accepts item prices and quantities and returns the total bill after applying a discount.
def calculate_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    # 10% discount
    discount = total * 0.10
    final_bill = total - discount

    return final_bill


prices = [100, 200, 300]
quantities = [2, 1, 3]

print("Total Bill after discount =", calculate_bill(prices, quantities))