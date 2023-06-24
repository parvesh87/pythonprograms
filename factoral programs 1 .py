a=int(input("enter the number:"))
even=0
for i in range (1,2*(a+1)):
    if(i%2==0):
        print(i)
        even=even+i
print(even)
