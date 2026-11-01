#13. Accept 10 numbers and sort them in:
   # •	Ascending order
    #•	Descending order
numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Ascending order
numbers.sort()
print("Ascending order:", numbers)

# Descending order
numbers.sort(reverse=True)
print("Descending order:", numbers)