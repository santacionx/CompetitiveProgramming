d={
    'hello':1,
    "a":20,
    3:14,
    'list':[1,2,3]
}
d['tuple']=(1,2,3)
print(d)
a={1:'a',3:11,"san":1000}
d.update(a)
print(d)
print(a.pop("san"))
a.clear()
del a
