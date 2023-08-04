class Bike:
    name="ktm"
    model="b53"
    engine=6
    gears=6
    tankcapcity=3
    mileage=70
    color="black"
    maxspeed=250

    def travel(self):
        print(self)
    def setproperty(self,n,m,e,g,t,mi,c,ms):
        self.name=n
        self.model=m
        self.engine=e
        self.gears=g
        self.tankcapcity=t
        self.mileage=mi
        self.color=c
        self.maxspeed=ms
    def displayproperty(self):
        print("name",self.name)
        print("model",self.model)
        print("engine",self.engine)
        print("gears",self.gears)
        print("tankcapcity",self.tankcapcity)
        print("mileage",self.mileage)
        print("color",self.color)
        print("maxspeed",self.maxspeed)

        
b=Bike()
##print(b.name)
b.setproperty("honda","d23",6,6,3,80,"black",240)
b.setproperty("
##print(b.name)
b.displayproperty()
print(b)


















##class Bike:
##    name="ktm"
##    model="b53"
##    engine=6
##    gears=6
##    tankcapcity=3
##    mileage=70
##    color="black"
##    maxspeed=250
##
##    def travel(self):
##        print(self.name)
##        
##b=Bike()
##b.travel()
##print(b)
