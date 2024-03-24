import time

def usingWhile(): 
    i = 0
    while i < 5:
      i = i + 1
      print(i)
  
def usingFor():
   for i in range(50):
      print(i)

init = time.time()
usingFor()
t1 = time.time() - init

init = time.time()
usingWhile()
print(t1)
print(time.time() - init)
