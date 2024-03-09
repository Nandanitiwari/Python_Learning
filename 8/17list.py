#list
marks = [98, 78, 89, "maths"]
print(marks)
print(marks[:])
print(marks[0])

print(marks[-1]) #from last
print(marks[-2]) #from last

print(marks[0:2]) #only 0 and 1

if "maths" in marks:
    print("yes")
else:
    print("No")

if "ths" in "maths":
    print("yes")
else:
    print("No")