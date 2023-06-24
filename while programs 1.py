num = int(input("enter the number"))


while num != 0:
    digit = num % 10
    num //= 10

print(digit)
