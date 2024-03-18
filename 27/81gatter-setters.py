#Gatters in Python are methods that are used to access the values of an object's
#properties. They are used to return the value of a specific property, and are typically defined using the @property decorator.

#to use gatter, we can create an instance of the MyClass class, and then access the value property as it si were an attribute

#Setters --> it is imp to node that getters do not take any parameters and we cannot set the value through gatter method.
#for that we need setter method which can be added by decorating method with @property_name.setter
class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property  # we can create a gatter by property dcorator
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67 #--> gives error can't set like this usse setter
print(f"value after mutiplying 10 is {obj.ten_value}")
obj.show()