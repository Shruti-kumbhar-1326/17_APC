#4.	Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p,r,t):
    si = (p*r*t) / 100
    return si
p = float(input("enter principle amount:"))
r = float(input("enter rate of interest:"))
t = float(input("enter time in years:"))
result = simple_interest(p,r,t)
print("simple Interest :",result)