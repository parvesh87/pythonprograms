a={"i":1,"v":5,"x":10,"l":50,"c":100,"d":500,"m":1000}
x={"iv":4,"ix":9,"xl":40,"xc":90,"cd":400,"cm":900}
b=input("enter the value:")
c=0
for i in a.keys():
    if(i in b):
        if(a in x):
            c+=a[i]
print(c)
