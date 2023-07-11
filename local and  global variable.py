##a=10
def myfunction():
    b=20
    b=50
    def innerfunction():
        b=202
        print("innerfunction",b)
    innerfunction()
    print("inside the function",b)
myfunction()
##print(a)


##def sum(n):
##    if(n!=0):
##        return n+sum(n-1)
##    else:
##        return 0
##print(sum(5))
