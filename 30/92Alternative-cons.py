#Class Method as Alternative Construtor
class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

class student:
    def __init__(self, word ):
        self.name = word

e = Employee("gunnu", 12000)
print(e.name)
print(e.salary)
string = "Harry-12000"
e = Employee(string.split("-")[0],string.split("-")[1])  #used to split the string
print(e.name)
print(e.salary)

str = "nannu-30000"
f = student(str.split("-"))
print(f.name)

