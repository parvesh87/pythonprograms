##def outer(func):
##    def inner(name):
##        print("Hello Good morning")
##        func(name)
##        print("Thank you")
##    return inner
##@outer
##def greeting(name):
##    print(f"hello {name},welcome to ocean academy")
##greeting("prem")


## Error
class GreaterThan100Error(Exception):
    def __init__(self,value):
        print("Greater than 100 error:given value is",value)
        
a=int(input("enter a number"))
try:
    if (a>100):
      raise GreaterThan100Error(a)
    else:
        print("a is less than 100")
except:
    print("error occurs")















    
