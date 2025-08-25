a = int(input("Enter num: "))
length = len(str(a))   # store number of digits
power = length
sum = 0
temp = a               # store original number

while a > 0:
    num = a % 10
    sum += num ** power
    a = a // 10

if temp == sum: 
    print("Armstrong")
else:
    print("Not Armstrong")