#2.	Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return"odd"
n = int(input("enter a num:"))
result = check_even_odd(n)
print("the number is:",result)    
    