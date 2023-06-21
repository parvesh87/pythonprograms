num=int(input("enter the number:"))
reversed_nums=0

while (num>0):
    last=num%10
    num=num//10
    reversed_nums=reversed_nums*10+last
    
print(reversed_nums)  

