time=input("enter time:")
day=input("enter day:")
duration=input("enter duration ")
a=int(duration[0:2])*60
b=int(duration[3:])
c=a+b
d=int(time[0:2])
if(day=="mo" or day=="tu" or day=="we" or day=="th" or day=="fr"):
    if(d>7 or d<18):
        print("The cost of call duration:",c*1.25)
    elif(d>18 or d<19):
        print("the cost of call duration:",c*1.15)
elif(day=="sa" or day=="su"):
    print("The cost of call duration :",c*1.15)
