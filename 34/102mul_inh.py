# mom + Dad = Children

class Employee:
    def __init__(self, name):
        self.name : name
    def show(self):
        print(f"the name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"the dance is {self.dance}")

class DancerEmployee(Employee, Dancer):  #employee is written first so "the name is shivani" will print by o.show() method
     def __init__(self, dance, name):
        self.dance = dance
        self.name = name

o = DancerEmployee("kathak", "shivani")
print(o.name)
print(o.dance)
o.show()

#mro() = "Method Resolution Order"
print(DancerEmployee.mro())
