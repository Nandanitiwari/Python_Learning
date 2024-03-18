class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
      print(f"the name of employee is {self.name} and id is {self.id}")

class programmer(Employee):
  def showLanguage(self):
     print("The default language is Python")

     
e1 = Employee("Roham Das" ,450)
e1.showDetails()

e2 = Employee("Sohan Das" ,650)
e2.showDetails()

e3 = programmer("gunnu", 780)
e3.showDetails()
e3.showLanguage()