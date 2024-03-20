class Employee:
    componyName = "Apple"  # these is class variable, these is associated with class, so bydefault all the instances in class will access(get) these
    def __init__(self,name):
        self.name = name 
        self.raise_amount = 0.02  #these are instance variable, instance variable are associated with instance not with class
    def showDetails(self):
        print(f"The name of the Employee is {self.name}, and the raise amount in compony {self.componyName} is {self.raise_amount}")

emp1 = Employee("Harry")
# (1 and 2 both are same)
emp1.showDetails()             #1
emp1.raise_amount = 0.3        #here we can change in instance variable
emp1.componyName = "Apple india"  #so here if there is an instance variable presend then the obj show that otherwise it will access the class variable
Employee.showDetails(emp1)     #2
# here in detail 1 is converted by 2, so that's why we have to pass self argument in showdetail function

print(Employee.componyName)
Employee.componyName = "Google"
print(Employee.componyName)

emp2 = Employee("Rohan")
emp2.componyName = "Nestel"
emp2.showDetails()

emp3 = Employee("Rohan")
emp3.showDetails() 