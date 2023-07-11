a={"i":1,"v":5,"x":10,"l":50,"c":100,"d":500,"m":1000}
x={"iv":4,"ix":9,"xl":40,"xc":90,"cd":400,"cm":900}
b=input("enter the value:")
temp=0
isPresent=0
for i in range(0,len(b)):
    data=b[i:i+2]
    if(data in x and isPresent==0):
        temp=temp+x.get(data)
        isPresent=1
    else:
        if(isPresent==0):
            temp=temp+a.get(b[i])
        else:
            isPresent=0
print(temp)
            
