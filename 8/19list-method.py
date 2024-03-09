#methods of list
marks = [98, 78, 89,  ]
marks.append(99)#add in last
marks.insert(0, 39) #from start
marks.sort()

print(marks)

marks.sort(reverse=True)
print(marks)

print(99 in marks)
print(len(marks))

if 98 in marks:
    print("yes")
else:
    print("No")

number = [6, 49 ,57, 89, 30 ,28  ]
print(number.index(49))

digit = number.copy()
digit[0] = 0
print(digit)
print(number)


number.reverse() #print the original list in reverse order
print(number)

