#Defining Custome Errors
class CustomError(Exception):
       pass
try:
      l = [1,5,6,7]
      i = int(input("Enter the index: "))
      print(l[i])
  
except CustomError:
       print("Some error occured")
 

e1 = CustomError("Roham Das" ,450)
e1.showDetails()

#complete it later