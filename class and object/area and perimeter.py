class Cirle:
    def area(self):
        print("area",3.14*self.radius**2)
    def perimeter(self):
        print("perimter",2*3.14*self.radius)

    radius=int(input("enter the radius"))
a=Cirle()
a.area()
a.perimeter()
    
