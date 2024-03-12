#list-comprehension
lst = [i for i in range(4)]
print(lst)
lst = [i*i for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)
