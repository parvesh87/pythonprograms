class LandlinePhone:
    name=""
    brand=""
    price=0
    noOfButtons=0
    iswired=False
    def makecall(self):
        print(self.name,"is used to make call")
    def receivecall(self):
        print("we receive calls")

class ButtonPhone(LandlinePhone):
    storagecapacity=0
    batterycapcacity=0
    screensize=0
    def messaging(self):
        print("we send and receive message")


a1=ButtonPhone()
a1.makecall()
a1.receivecall()
a1.messaging()
