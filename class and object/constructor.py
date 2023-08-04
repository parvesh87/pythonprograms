class Student:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
        print("constructor is running")
    def setproperty(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def reading(self):
        print(self.name,"is reading")
    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("mark",self.mark)


s1=Student("siva",20,460)
s1.display()
s1.setproperty("sai",50,350)
s1.display()
