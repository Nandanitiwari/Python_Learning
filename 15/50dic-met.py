ep1 = {122 : 45, 123 : 89, 124 : 34, 125 : 78}
ep2 = {126  : 78, 127 : 90, 128 : 67, 130 : 57}

ep1.update(ep2)
print(ep1)

ep1.pop(122)
print(ep1) 

ep1.popitem()
print(ep1)

del ep1[123]
print(ep1)

ep1.clear()
print(ep1)

empt = {} #it is an empty dictonary
print(empt)

