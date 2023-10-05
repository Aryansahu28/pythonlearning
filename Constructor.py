class Person:
    def __init__(self):
        print("Hey I am a person")

    def info(self):
        print(f"{self.name} is a {self.occupation}")


    
a = Person()
a.name = "Shivam"
a.occupation = "Businessman"

a.info()