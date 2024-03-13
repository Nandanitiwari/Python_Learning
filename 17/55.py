#Finally Clause
def func1():
  try:
    l = [1,5,6,7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occured")
    return 0

# when we wrap the whole block in a function then finally statement will execute but a simple print a statement will not be executed
  finally:
    print("I am always executed")

x = func1()
print(x)