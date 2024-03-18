# Q). To create method on class, is it important to pass self argumeny? 
# Ans). No bcs of static method

#we use static methods when we do not use Class or instance
class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    #here we do not need ot use self in staticmethod 
    #these is not assosiate with instance or class  
    @staticmethod  
    def add(a,b):
        return a + b
    
    
# result = Math.add(1, 2)
# print(result)
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

#staticmethod can call using both method and class name
print(a.add(7, 2))
print(Math.add(7, 2))
