def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

def add(a, b):
    print(a+b)

greet(add)(1, 2)

#decorators are a poerful and flexible feature in python that can be used to add functionality to functions and methods without modifying their source code.
#they are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.