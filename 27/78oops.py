#classes and objects
# SELF PARAMETER --> the self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
#self means the object for which the method is being called ---> (a)
class Person:
    name = "Gunnu"
    occupation = "software developer"
    networth = 1000000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "shubham"
a.occupation = "Accountant"
print(a.name, a.occupation, a.networth)
a.info()