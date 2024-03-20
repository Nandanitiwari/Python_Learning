#class method is a type of method that is bound to the class and not the instance of the class.
class Employee:
    company = "Apple"
    def show(self):
        print(f"the name is {self.name} and compony is {self.company}")
#it will change tshe class variable directly    
    @classmethod  #it will reference the variable of class
    def changeCompony(cls, newCompony):
        cls.company = newCompony

e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompony("Tesla")
e1.show()
print(Employee.company)  #it will point class variable and print tesla bcs of classmethod