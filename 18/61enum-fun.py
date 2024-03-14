#Enumerated Function

marks  = [12, 35, 56, 78, 89, 45 ]
 
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#       print("awesome!")
#     index = index + 1

# print("----- end ----- ")

# for i, mark in enumerate(marks):
#      print(mark)
#      if(i == 3):
#       print("awesome!")

# print("----- end ----- ")

for i, mark in enumerate(marks, start=2): #here start define the exact position means i == 3 means not index but from starting 1 the thirsd value, if start = 2 then 3rd value + 1
     print(mark)
     if(i == 3):
      print("awesome!")
  