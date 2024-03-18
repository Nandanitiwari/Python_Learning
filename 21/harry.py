def welcome():
    print("Hey you are welcome from harry")

print(__name__)
#if it run from here then the value will be main
#if it run from other file the value will be harry 
if __name__ == "__main__": #it means if it run from here then run the next line welcome function otherwise not
   welcome()