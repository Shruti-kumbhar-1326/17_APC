#Write a PYTHON program that prints  1 2 4 8 16 32 … n2
n = int(input("Enter the value of n: "))
i = 0
while i <= n:
    print(2 ** i, end=" ")
    i += 1
