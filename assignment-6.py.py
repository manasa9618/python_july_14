a={"name": 'manasa',"section": 'mca',"rollno": '46',"mail-id": 'manu@gmail.com',"marks": '99'}
keys = a.keys()
print(keys)
values = a.values()
print(values)
items = a.items()
print(items)
print(a)
a.update({"address": 'hyd'})
print(a)
a.update({"place" : 'rgp'})
print(a)
a.pop('place')
print(a)
print(a.get("name"))
print(a.get("gender"))
print(a.get("gender",-1))
print(a['mail-id'])

#set operations

a1={1,2,3,5,7}
b1={6,2,9,48,0}
print(a1.union(b1))
print(a1.intersection(b1))
print(a1.difference(b1))
print(a1.symmetric_difference(b1))

#set

d={1,3,2,5,3,2,7,6,5}
print(d)
d.add("shreya")
print(d)
d.remove(3)
print(d)
d,update("shreya,manasa")
print(d)


