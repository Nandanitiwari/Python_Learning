s1 = {1, 2, 3, 4, 5}
s2 = {4, 7, 9, 61, 23}
print(s1.union(s2))
print(s1, s2)
s1.update(s2)
print(s1, s2)
print(" ")

cities = {"usa", "seoul", "berlin","delhi"}
cities2 = {"tokyo", "seoul", "berlin", "mardin"}
cities3 = cities.intersection(cities2)
print(cities3)

city = {"usa", "seoul", "berlin","delhi"}
city2 = {"tokyo", "seoul", "berlin", "mardin"}
city.intersection(city2)
print(city2)
print(" ")

cities4 = cities.symmetric_difference(cities2) #value which are diff in both set
print(cities4)

c1= {"tokyo", "seoul", "berlin", "mardin"}
c2 = {"usa", "seoul", "berlin", "mardin"}
c3 = c1.difference(c2) #value which are only in set1
print(c3)
print(" ")

place = {"garoth", "ratlam", "alot", "suwasra"}
place2 = {"garoth", "ujjain", "agra", "suwasra"}
print(place.isdisjoint(place2)) #nothing shoud be common no intersection

print(" ")

location= {"garoth", "ratlam", "alot", "suwasra"}
location2 = {"garoth", "suwasra"}
print(location.issuperset(location2))
print(location2.issubset(location))

location3 = {"usa", "seoul","ujjain", "agra",}
print(location.issuperset(location3))
print(" ")

a1 = {"riya", "priya", "supriya", "kavya"}
a1.add("alka")
print(a1)

a2 = {"rahu", "gopi","sonu","rinku"}
a2.remove("rahu") #remove the value if present else give error
print(a2)

a3 = {"rahu", "gopi","sonu","rinku"}
a3.discard("rahul") #remove the value if present if not present did not give error error
print(a3)
print(" ")

a4 = {"delhi", "usa", "uk", "shimla"}
item = a4.pop()
print(a4)
print(item)

a5 = {"delhi", "usa", "uk", "shimla"}
del a5  #delete the entier set
#print(a5) 
# #not printing a5 bcs a5 is deleted

a6 = {"delhi", "usa", "uk", "shimla"}
a6.clear() #set is present but elements is deleted
print(a6)