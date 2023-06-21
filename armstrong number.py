num = int(input("Enter a number: "))
a=0
sum=0
temp=num

while num > 0:
   last=num%10
   sum = last**3
   a=a+sum
   num=num//10


if (temp==a):
    print(temp,"is an Armstrong number")
else:
    print(temp,"is not an Armstrong number")




      
