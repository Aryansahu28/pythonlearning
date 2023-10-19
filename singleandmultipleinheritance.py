class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def show_Employee_detail(self):
        print(f"{self.name} has id {self.id}")

class Dancer(Employee):
    def __init__(self,name,id,dancestyle):
        super().__init__(self,name,id)
        self.dancestyle = dancestyle

class Programmer:
    def __init__(self,lang,eid):
        self.lang = lang
        self.eid = eid
    
class Dual(Employee,Programmer):
    def __init__(self,dual):
        self.dual = dual

    def showDetail(self):
        print(f"{self.name} is a dancer of {self.dancestyle} ")


e1 = Employee("Aryan", 2345)

e2 = Dancer("Garba")
e3 = Programmer("Python",45645)
e4 = Dual("Classic")

e4.showDetail()

