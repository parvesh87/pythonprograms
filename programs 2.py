a=input("enter the number:")
if (len(a)>=3):
    if a[-3:]=="ing":
        c=a+"ly"
    else:
        c=a+"ing"

else:
    c=a+"ing"

print(c)    

