class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang) :
    #    self.name = name
    #    self.id = id
       super().__init__(name, id)   #to reduce repeate
       self.lang = lang   

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(rohan.name)
print(harry.name)
print(harry.id)
print(harry.lang)
