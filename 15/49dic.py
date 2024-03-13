dic = {
  "Name" : "gunnu",
  id : 45,
  45000: "salary"
}
print(dic)
print(dic.keys())
print(dic["Name"])
print(dic[id]) #it will give error if key(id) is not written correct

print(dic.get(id)) #it will not give error just print None, if key does'nt exist

for keys in dic.keys():
    print(dic[keys])

for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")