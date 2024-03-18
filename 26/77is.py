# 'is' vs '=='
#both are comparison operator
#is --> return true when identity is same(means that is only one object but having different name)
#== --> return true when when value of object is same

a = 4  #this is integer
b = "4"  #this si string
print(a is b) #exact location of object in memory
print(a == b) #value

#when we create a constant in python so it created only one time in memory location bcs python know that the constant will not be changed bcs it is immutable so python did not waste the memory location, pytjon will use the leverage, so here a and b are pointing the same memory location where 3 is stored
a2 = 3
b2 = 3
print(a2 is b2) 
print(a2 == b2)

#but here list may get changed in future as compared to constants
a3 = [1, 2, 3]
b3 = [1, 2, 3]
print(a3 is b3)
print(a3 == b3)

#tuples are immutable(can't change) so python stored it only once same as constants
a3 = (1, 2)
b3 = (1, 2)
print(a3 is b3)
print(a3 == b3)

a4 = None
b4 = None
print(a4 is b4)
print(a3 == b3)
print(a4 is None)
print(b4 is None)