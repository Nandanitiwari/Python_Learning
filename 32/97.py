#Dunder methods --> magic mehods
# special methods define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.
#from the double underscore () surrounding their names, are powerful tools that allow you to customize the behaviour of your classes.
#used to implement special methods such as the addition,subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

class Employee:
     name = "gunnu"
     def __len__(self):
         i = 0 
         for c in self.name:
           i = i + 1
         return i   
     
e = Employee("Harry")
# print(e.name)
# print(len(e))