#tuple-can't change tuple
#tuples are [{(IMMUTABLE)}]
marks = (98, 34, 78, 56, 90, 99, 90, 78, 90)
#marks[0] = 99 cna'n change
# res = marks.count(90)
print("count of 3 in tuple is" , marks.count(90))
# pos = marks.index(90)
print("first index of 0 is" , marks.index(90))

num = (98, 34, 78, 56, 90, 99, 90, 78, 90)
res = num.index(90, 4, 8)
print("count of 90 in between 4 to 8 is:-", res)
length = len(num)
print("Length of tuple is:- ", length)
#tuple is ordered bcs index exist here
