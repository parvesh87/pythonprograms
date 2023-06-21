a=int(input("enter the killometer travelled by you"))
if(a<10):
    print("the cost is = ",a*11)
elif(a>=10 and a<=90):
    print("the cost is = ",a*10)
elif(a<=90):
    print("the cost is =", a*9)
