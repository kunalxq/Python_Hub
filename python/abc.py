a = int(input("enter a num :"))
large = 0
while a>0:
 digit = a % 10
 if digit > large:
     large = digit
     a = a // 10
     print(large)