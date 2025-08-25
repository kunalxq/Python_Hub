num = int(input("enter num:"))
deci = 0
power = 0

while num > 0:
    digit = num % 10
    deci += digit * (2 ** power)
    power += 1
    num //= 10
print(deci)