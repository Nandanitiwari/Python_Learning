countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russai") #add item
print(temp)

temp.pop(3)   #remove item
print(temp)

temp[2]="Finland"  #change item
print(temp)

countries = tuple(temp)
print(countries)
