# Generators in python are special type of function that allow you to create an iterable sequence of values.
# A generator function a generator object, which can be used to generate the value one-by-one as you iterate over it.
# Generators are a powerful tool for working with large or complex data sets,as they allow you to generate the values on-the-fly, 
# rather than having to create an store the entire sequence in memory

#"yield" keyword returns a value from the generator and suspend the execution of the function until the next requested.
def my_generator():
    for i in range(5):
        #if there is any complex computation than, that computation will perform for every execution
        yield i

gen = my_generator()
print(next(gen))        #--> gives output 0
print(next(gen))        #--> gives output 1
print(next(gen))        #--> gives output 2
print(next(gen))        #--> gives output 3

# for j in gen:
#     print(j)     #if above print statement is present than it will print next value, otherwise it will print the overall value till the range