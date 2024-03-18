class Student:
     def __init__(self):
        self._name = "gunnu"

     def _funName(self):
        return "codewithharry"

class Subject(Student):
     pass

obj = Student()
obj1 = Subject()
print(dir(obj))

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())