class Mobilephone:
    def __init__(self,name,brand,color,weight,processor,andriodversion,ram,storage):
        self.name=name
        self.brand=brand
        self.color=color
        self.weight=weight
        self.processor=processor
        self.andriodversion=andriodversion
        self.ram=ram
        self.storage=storage
    def setproperty(self,name,brand,color,weight,processor,andriodversion,ram,storage):
        self.name=name
        self.brand=brand
        self.color=color
        self.weight=weight
        self.processor=processor
        self.andriodversion=andriodversion
        self.ram=ram
        self.storage=storage
    def browse(self):
        print(self.name,"you can browse information")
    def display(self):
        print("name",self.name)
        print("brand",self.brand)
        print("color",self.color)
        print("weight",self.weight)
        print("processor",self.processor)
        print("andriodversion",self.andriodversion)
        print("ram",self,ram)
        print("storage",self.storage)

b=Mobilephone("vivo","t1","black",18.5,662,13,128)
b.display()

