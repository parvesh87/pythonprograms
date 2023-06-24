num=int(input("enter the number:"))
s=0

while(num>0):
    last=num%10
    s=s+last
    num=num//10
print("sum of digits is",s)
    
