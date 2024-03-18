#SEEK() AND TEEL FUNCTION

#SEEK()
with open('73a.txt', 'r') as f:
    print(type(f))
    #move to the 10th byte in the file
    f.seek(10)

    print(f.tell())

    #Read the next 5 bytes
    data = f.read(5)
    print(data)

#TEEL() -- return the current position within th file, in bytes.
#TRUNCATE() -- size file character
with open('73b.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(3)

with open('73b.txt', 'r') as f:
    print(f.read())
