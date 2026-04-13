a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print(f"Max: {maximum}")