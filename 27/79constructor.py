#constructor helps to create an object
#A constructor is a special method in class and initialize an object of a class.
#there are different types of constructors
#Constructor is invoked automatically when an object of a class is created
#Aconstructor is a unique function that gets called automatically when an object is created of a class.
# The main purpose of a constructor is to initialize or assign values to the data members of that class.
# It cannot return any value other that None


#init is one of the reserved functions in python In OOP. It is known as a constructor 
#We can also create constructor by defining the function name with same class name
class Person:
    # name = "gunnu"
    # occ = "Developer"  --> without doing this we can create a constructor

    def __init__(self, n, o):  # --> called dunder method
      print("Hey i am a Person")
      self.name = n
      self.occ = o

    def info(self):
       print(f"{self.name} is a {self.occ}")

a = Person("gunnu", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()
# gives 4 argument error bcs one argument is (c --> self)
#c = Person(1, 2, 3)   -->parameterized constructor accept aargument along with self

#gives missing 2 positional arrgument(n , o) argument error
#d = Person()  --> default constructor accepts only self argumet