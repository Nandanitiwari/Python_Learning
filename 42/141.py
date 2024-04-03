a = 5             # taking 3 bit (101)
b = 6             # taking 3 bit (110)

#method 1         --> using a new temporary variable
# temp = a
# a = b
# b = temp

#method 2        --> we can do it without using 3rd variable
# a = a + b       # 11 -> taking 4 bit (wasting 1 extra bit)
# b = a - b
# a = a - b

#method 3       --> using XOR 
# a = a ^ b       
# b = a ^ b
# a = a ^ b

#method 4
a,b = b,a

#Print statement
print(a)
print(b)


