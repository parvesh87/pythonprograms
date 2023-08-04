class Calculator:
    x=int(input("enter the value 1:"))
    y=int(input("enter the value 2:"))
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y

    
b=Calculator()
print("add",b.add())
print("sub",b.sub())
print("mul",b.mul())
print("div",b.div())
