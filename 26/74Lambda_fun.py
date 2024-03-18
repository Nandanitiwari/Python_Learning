#LAMBDA function :-
# in python a lambda function is a small anonymous function
# without a name. It is a defined using the lambda keyword 

#FUNCTION TO DOUBLE THE INPUT
def square(x):
    return x * 2

print(square(5))

def apply(fx, value):
    return 6 + fx(value)

#LAMBDA FUNCTION
square = lambda x : x * 2
print(square(5))

cube = lambda x : x * x * x
print(cube(5))

avg = lambda x, y, z:(x + y + z)/3
print(avg(3, 5, 6))

print(apply(cube, 2))
print(apply(lambda x : x * x * x, 2))