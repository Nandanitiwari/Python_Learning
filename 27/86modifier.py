class Employee:
    def __init__ (self):  
        self.name = "Harry"
        # weak internal use indicator
        self.__name = "gunnu"
    

a = Employee()
print(a.name)
# print(a.__name)   --> it will give error
#it is called name mangling -it is used to protect class private and superclass-private attribute from being accidently overwritten by subclasses
print(a._Employee__name)  #for weak (private)
print(a.__dir__())


# the single underscore is just a naming convention and doed not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variabe name followed by a single underscore(_)ie. _variable