a = int(input("enter num1:"))
b = int(input("enter num2:"))

for i in range(max(a,b), ((a+1) * (b+1))):
    if i % a == 0 and i % b == 0:
        lcf=i
        print(lcf)