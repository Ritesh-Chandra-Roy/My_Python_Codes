a = {10, 20, 20, 30, 10, 40, '40'}
print(type(a))
# print(a)
#Empty set
# b = {} This is empty Dictionary
b = set() #Empty Set Created
# print(type(b))
#Methods
b.add(7)
b.add(11)
b.add(7)
# b.add([100, 200, 300]) cannot add list to set coz lists & Dictionary are not hashable
b.add((10, 12, 14)) #adding Touple
# print(b)
#MEthods
print(len(b))
b.remove(11)
# print(b)
print(a.pop()) #Removes an arbitrary element
b.add(20)
a.add(7)
c = a.union(b)
print(c)
d = a.intersection(b)
print(d)
#https://www.w3schools.com/python/python_sets_methods.asp for more methods