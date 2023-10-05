class Person:
    name = "Harry"
    occupation = "Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = Person()

a.name = "Ravi"
a.occupation = "Hacker"
a.info()
b = Person()
b.info()

