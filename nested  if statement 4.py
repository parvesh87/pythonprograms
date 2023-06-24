age=int(input("enter the age"))
gender=input("enter the Gender")
days=int(input("number of days "))
if age>=18 and age<30:
    if gender=="Male" or gender=="Male":
        print("your wage per day is =700 total wages =",700*days)
    elif (gender=="female" or gender=="female"):
        print("your wageper day is= 750 total wages =",750*days)
    else:
        print("invalid Gender")

if age>=30 and age<=40:
    if gender=="male" or gender=="male":
        print("your wage per day is =800 total wages =",800*days)
    elif(gender=="female" or gender=="female"):
        print("your wage per day is =850 total wages =",850*days)
    else:
        print("invalid gender")
else:
    print("appropriate age")
    
