class EvenError(Exception):
    def __init__(self,value):
        print("even error:given value is",value)
        
a=int(input("enter a number"))
try:
    if (a>100):
      raise  EvenError(a)
    else:
        print(" the number is odd")
except:
    print("error occurs")




