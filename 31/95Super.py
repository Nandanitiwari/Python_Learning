class ParentClass:
    def parent_method(self):
        print("this is the parent method.")  #this will run when parent_method() of child class is not present

class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry")
        super().parent_method()
    def child_method(self):
        print("this is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()