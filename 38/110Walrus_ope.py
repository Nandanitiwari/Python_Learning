# Walrus operator  --> [:=]
a = True
print(a:=False) 

#example 1
num = [1,2,3,4,5]
while ( n:= len(num)) > 0:
    print(num.pop())

#example 2
names = ["john", "jin", "jimin"]

if(name := input("Enter a name:"))in names:
    print(f"Hello, {name}!")
else:
    print("Name not found")