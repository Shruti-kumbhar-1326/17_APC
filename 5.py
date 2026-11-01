#Write a PYTHON program to sum the given sequence  1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!
n = int(input("Enter the value of n: "))

fact = 1
sum = 1  # First term of the sequence

for i in range(1, n + 1):
    fact = fact * i      # Calculate i!
    sum = sum + (1 / fact)

print("Sum of the series =", sum)