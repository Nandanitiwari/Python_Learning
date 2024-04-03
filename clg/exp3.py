#Q1)using a for loop,Wap that prints out the decimal equivelents of 1/2, 1/3, 1/4...1/10
for i in range(2,11):
   print(1/i)

#Q2)write a programme using a for loop that loops over a sequence
Color_list = ['red','green', 'white','purple','maroon']
for i in Color_list:
   print(i)

#Q3).Sum of list of elements
Num = [1,2,3,4,5,6,7,8,9,10]
Sum = 0
for i in Num:
   Sum = Sum + 1
   print(Sum)

#Q4).for loop in string
fr_string = 'goadhub_technologies'
for i in fr_string:
   print(i) 

#Q5). for loop in dictionary
fr_dict = {1:'q',2:'w',3:'c',4:'r'}
for i in fr_dict:
   print(i)
   print(fr_dict)

#Q6).take input from user and print it in reverse order
num = int(input("enter your number"))
while(num>0):
  print(num)
  num = num-1
