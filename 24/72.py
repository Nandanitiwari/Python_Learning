# f = open('72a.txt','r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#       break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"marks of student {i} in maths is: {m1*2}")
#   print(f"marks of student {i} in english is: {m2*2}")
#   print(f"marks of student {i} in science is: {m3*2}")

#   print(line)

#WRITELINE() METHOD DOES'NT GIVE NEW-LINE
# f = open('72b.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()


f = open('72c.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()