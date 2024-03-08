first = input("enter first number :")
operator = input("enter operator(-,*,+,/) :")
second = input("enter second number :")

if operator == "+":
    print(int(first) +  int(second))

elif operator == "-":
    print( int(first) -  int(second))

elif operator == "*":
    print( int(first) * int(second))

elif operator == "/":
    print( float(first) /  float(second))

else:
    print("wrong input")
   