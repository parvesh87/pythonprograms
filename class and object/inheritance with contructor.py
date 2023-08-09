class LandlinePhone:
    def __init__(self,name,brand,price,noOfButtons,iswired):
        self.name=name
        self.brand=brand
        self.price=price
        self.noOfButtons=noOfButtons
        self.iswired=iswired
    def makecall(self):
        print(self.name,"is used to make call")
    def receivecall(self):
        print("we receive calls")

class ButtonPhone(LandlinePhone):
    def __init__(self,name,brand,price,noOfButtons,iswired,
                 storagecapacity,batterycapcacity,screensize):
        super().__init__(name,brand,price,noOfButtons,iswired)
        self.storagecapacity=storagecapacity
        self.batterycapcacity=batterycapcacity
        self.screensize=screensize
    def messaging(self):
        print("we send and receive message")
    def display(self):
         print("name",self.name)
         print("brand",self.brand)
         print("price",self.price)
         print("noOfButtons",self.noOfButtons)
         print("iswired",self.iswired)
         print("storagecapacity",self.storagecapacity)
         print("batterycapcacity",self.batterycapcacity)
         print("screensize",self.screensize)
        


a1=ButtonPhone("s25","vivo",5000,10,False,128,5000,20)
a1.display()
a1.makecall()
##a1.receivecall()
##a1.messaging()
