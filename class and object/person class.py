class Person:
    name="king"
    country="India"
    dataofbirth="20.7.2008"
    a=int(dataofbirth[-4::])
    b=2023

    def age(self):
        print(self.b-self.a)


g=Person()
g.age()
    
