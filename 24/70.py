# 70

# r = this mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter
#rt = opens as text file
#rb = opens as binary file

#READING A FILE
# f = open('b.txt' , 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

#WRITING TO A FILE
# g = open('c.txt', 'w')  #In write mode if you opens a file which does not exist then thefile will be created it will add contain only one time
# g.write('you are awesome!')
# g.close()

g = open('70c.txt', 'a')  #In write mode if you opens a file which does not exist then thefile will be created it will add contain only one time
# g.write('you are awesome!')
# g.close()

with open('70c.txt', 'a'):  #it will create a file if already created then write the containt and close the file
    g.write("Hey I am inside with")