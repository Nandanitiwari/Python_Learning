#MAP, FILTER , REDUCE  => these are higher order function
def cube(x):
    return x * x * x

print(cube(3))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1.
newl = []
for item in l:
    newl.append(cube(item))
print(newl)

# 2.
#syntax = conversion(map(fun_name, iterable))
#MAP
nl1 = map(cube, l)
print(nl1)

newlist = list(map(cube, l))
print(newlist)

thelist = list(map(lambda x : x * x * x, l))
print(thelist)

#FILTER
def filter_fun(a):
    return a>4

nl = filter(filter_fun, l)
print(nl)

newlist2 = list(filter(filter_fun, l))
print(newlist2)

thelist2 = list(filter(lambda a : a > 4, l))
print(thelist2)