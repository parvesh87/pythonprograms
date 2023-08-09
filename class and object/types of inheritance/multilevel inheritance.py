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
class Mobilephone(ButtonPhone):
    def __init__(self,name,brand,price,noOfButtons,iswired,
                 storagecapacity,batterycapcacity,screensize,
                     displaySize,microphone,vibratormotor):
        super().__init__(name,brand,price,noOfButtons,iswired,storagecapacity,batterycapcacity,screensize)
        self.displaySize=displaySize
        self.microphone=microphone
        self.vibratormotor=vibratormotor
    def videocall(self):
        print("is used to make video call")
    def receivevideocall(self):
        print("we receive the video call")
        
    def displayProperty(self):
         print("name",self.name)
         print("brand",self.brand)
         print("price",self.price)
         print("noOfButtons",self.noOfButtons)
         print("iswired",self.iswired)
         print("storagecapacity",self.storagecapacity)
         print("batterycapcacity",self.batterycapcacity)
         print("screensize",self.screensize)
         print("displaySize",self.displaySize)
         print("microphone",self.microphone)
         print("vibratormotor",self.vibratormotor)
        


a1=Mobilephone("s25","vivo",5000,10,False,128,5000,20,"OLED",True,True)
a1.displayProperty()
