def outer():
    def inner():
        print("inner function")
        return "hello"
    print("outer function")
    return inner
x=outer()
inner()
x()

##def display(a):
##    print("hello")
##    print(a)
##def outerfunction(func):
##    print("good morning")
##    func("thank you")
##outerfunction(display)
##
##def greeting():
##    print("hello, Good morning")
##
##print("welcome to ocean academy")
##greeting()
##print("thank you")
##     
