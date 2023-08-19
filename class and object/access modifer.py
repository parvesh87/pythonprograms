class Person:
    def __init__(self,name,age):
        self._name=name
        self.age=age
    def dispayProperty(self):
        print(f"person name:{self.__name}\nage={self.age}")
class Student(Person):
    def __init__(self,name,age,mark):
        super().__init__(name,age)
        self._mark=mark
    def getMark(self):
        return self._mark
    def setMark(self,mark):
        self._mark=mark
    def displayProperty(self):
        print(f"Student name:{self._name}\nage={self.age}\nmark={self.__mark}")

a=Student("dhev",25,450)
a.displayProperty
print(a.getMark())
a.setMark(440)
print(a.getMark())
