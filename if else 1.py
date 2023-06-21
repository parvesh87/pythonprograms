eng=int(input("enter english mark"))
math=int(input("enter maths mark"))
sci=int(input("enter science mark"))
soc=int(input("enter social science mark"))

if(eng>=40 and math>=40 and sci >=40 and soc>=40):

    if (eng>=80 and math>=80 and sci>=80 and soc>=80):
        print("science stream")
    elif(eng>=80 and math>=50 and sci>=50):
        print("commers stream")
    elif(eng>=80 and soc>=80):
        print("humanities")

else:
    print("not able to find a group")
