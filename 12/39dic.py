#Dictonary= []
def name(**name):
    print(type(name))
    print("Hello,", name["fname"],
    name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname="james")