#Decorators
#Decorators are poweful and versatile tool that allow you to modify the behaviour of fumctions and methods. 
#They are a way to extend the functionality of a function or method without modifying its source code

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx
    
@greet
def hello():
    print("Hello world")

hello()