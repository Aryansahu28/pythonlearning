class Employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id

    def showDetails(self):
        print(f"{self.id} id is belong to {self.name}")


class Programmer(Employee):
    def showAge(self):
        print(f"{self.name} has age of {int(self.id)/100}")


e1 = Employee("Kumar Sanu",1294)

e1.showDetails()

e2 = Programmer("Gojo Sataru",12454)
e2.showAge()


