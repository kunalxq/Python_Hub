a = int(input("enter a number:"))
b = " "
while a > 0:
    r = a % 2 
    b = b+str(r)
    a = a // 2
print(b[::-1])