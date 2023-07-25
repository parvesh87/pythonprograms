x=int(input("enter the word:"))
a=0
for i in range(1,x):
    if x%i==0:
        a=a+i
        
if a==x:
    print("perfect number")
else:
    print("not a perfect number")
