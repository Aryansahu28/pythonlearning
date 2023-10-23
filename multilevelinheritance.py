class Animal:
    def __init__(self,name, species):
        self.name = name
        self.species = species

    def show_Animal(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

    
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def show_name(self):
        Animal.show_Animal(self)
        print(f"Breed : {self.breed}")


class GoldenRetriever(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="GoldenRetriever")
        self.color = color

    def show_detail(self):
        Dog.show_name(self)
        print(f"Color : {self.color}")


o = GoldenRetriever("Browny","Brown")

o.show_detail()

    