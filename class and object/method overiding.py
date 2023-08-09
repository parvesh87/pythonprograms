class RBI:
    def __init__(self,name):
        self.name=name
    def getinterest(self):
        print(f"{self.name} bank provide interest of 7% for home loan")
class SBI(RBI):
    pass
class ICICI(SBI):
    def getinterest(self):
        print(f"{self.name} bank provide interest of 6.6% for home loan")
ic=ICICI("icici")
ic.getinterest()
sb=SBI("sbi")
sb.getinterest()
