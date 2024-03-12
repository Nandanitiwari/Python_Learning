#1
def average(a,b):
      print("The average is", (a+b)/2)

average(4,6)

#2
def average(c,d=2):
      print("The average is", (c+d)/2)

average(4)

#3
def average(a=5,b=7):
      print("The average is", (a+b)/2)

average()
#4
average(b=9, a=5)#keyword argument

#5
def avg(a,b,c=2):
      print("The average is", (a+b+c)/2)

avg(5,7)