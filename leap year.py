year=int(input("enter the year"))
if(year%100==0):
    print("century year")
    if(year%400==0):
        print("it is leap year")
    else:
        print("it is not leap year")
else:
    if (year%4==0):
        print("it is leap year")
    else:
        print("itis not leap year")
         
