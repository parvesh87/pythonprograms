##a=[]
##for i in range(3):
##    a.append([])
##    for j in range(3):
##        temp=int(input("enter a number:"))
##        a[i].append(temp)
##print(a)




a=[]
b=int(input("enter a number:"))
c=int(input("enter a number:"))
for i in range(b):
    a.append([])
    for j in range(c):
        temp=int(input("enter a number:"))
        a[i].append(temp)
print(a)



x=[]
for i in range(b):
    x.append([])
    for j in range(c):
        temp=int(input("enter a number:"))
        x[i].append(temp)
print(x)

for i in range(b):
    for j in range(c):
        d=(a[i][j])
        e=(x[i][j])
        print(d+e,end=" ")
    print()
        
