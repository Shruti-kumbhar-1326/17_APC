# 23. Calculate bill details

prices = (100, 250, 150, 500, 300)

total = 0

for price in prices:
    total = total + price

average = total / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

print("Total bill:", total)
print("Average price:", average)
print("Highest price:", highest)
print("Lowest price:", lowest)