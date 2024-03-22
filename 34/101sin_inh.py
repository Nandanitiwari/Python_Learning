class Animal:
    def __init__(self, name, species):
        self.name = name
        # self.sound = sound
        self.species = species
    
    def make_sound(self):
        print(f"Sound made by the animal {self.name} ")

class Dog(Animal):
    def __init__(self, name , bread):
        Animal.__init__(self, name, species = "Dog")
        self.bread = bread

    def make_sound(self):
       print("Bark!")

d = Dog("tomy", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()