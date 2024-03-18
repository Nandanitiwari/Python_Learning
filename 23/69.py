#local ang global variable
x = 4  #global variable
print(f"the global x is {x}")
y = 10

def hello():
  x = 5  #local variable
  print(f"The Local x is {x}")
  print(f"The Global y is {y}")
  print("Hello harry")

print(f"the global x is {x}")
hello()
print(f"the global x is {x}")

print("-----second phase------")
a = 10
def myfun():
  global a
  a = 3
  print(a)

myfun()
print(a) #here a=3 printed not 10 bcs a=3 is global