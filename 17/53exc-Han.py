a = input("enter the number: ")
print(f"Multiplication table of {a} is:")

try:
   for i in range(1, 11):
    print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
  print(f"you entered a wrong input {a} please enter an integer")


print("Some lines of code")
print("End of program")