# Write a PYTHON program to compute the cosine series cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

sum = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1

    # Calculate i!
    for j in range(1, i + 1):
        fact = fact * j

    term = (x ** i) / fact
    sum = sum + (sign * term)

    sign = sign * -1   # Change sign (+/-)

print("cos(", x, ") =", sum) 

