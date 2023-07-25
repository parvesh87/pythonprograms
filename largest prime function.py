##x=int(input("enter the word:"))
##z=0
##for i in range(1,x+1):
##    if(x%i==0):
##        z=z+i
##        print(z)
##
##
##
##a=int(input("enter the number:"))
##temp=0
##for i in range(2,a):
##    if(a%i==0):
##        print("not a prime")
##        temp+=1
##          break
##    elif(temp==z):
##        
##
##if (temp==0):
##    print("prime number")
##          
##

n=int(input("enter a number"))
x=0
a=[]
b=[]
for i in range(1,n+1):
    if(n%i==0):
        a.append(i)
        print(a)
        for j in range(2,n):
            if(j==0):
              x+=1
              break
        if(x==0):
            b.append(x)
            print(b)















            
            
