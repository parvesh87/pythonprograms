a=int(input("enter the number:"))
temp=0
for i in range(2,a):
    if(a%i==0):
        print("not a prime")
        temp+=1
        break

if (temp==0):
    print("prime number")
          
