# grand father --> father --> Son

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name , bread):
        Animal.__init__(self, name, species = "Dog")
        self.bread = bread
    
    def show_details(self):
        Animal.show_details(self)
        print(f"Bread: {self.bread}")
  
class GolderRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, bread="Golder Retriever")
        self.color = color

    def show_details(self):
       Dog.show_details(self)
       print(f"Color : {self.color}")

o = GolderRetriever("Tomy", "Black")
o.show_details()

d = Dog("moti", "Doggerman")
d.show_details()

a = Animal("shiro", "indian")
a.show_details=()

print(GolderRetriever.mro())