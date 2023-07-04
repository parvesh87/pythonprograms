##a=int(input("enter the number"))
##if a>0 and a<10:
##      print("the give number",a, "is single digited")
##elif a>10 and a<100:
##    print("the give number" ,a, "is double digited")
##elif a>100 and a<1000:
##    print("the give number",a,"is three digited")
##else:
##    print("the give number",a, "is four digited")




a=int(input("enter the number 1"))
b=int(input("enter the number 2"))
c=int(input("enter yhe number 3"))
if a>b and a>c:
    print("a is greater number")
elif b>a and b>c:
    print("b is greater number")
elif c>a and c>b:
    print("c is greater number")
else:
    print("invalid input")
