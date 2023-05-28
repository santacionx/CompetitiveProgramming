d={
    'hello':1,
    "a":20,
    3:14,
    'list':[1,2,3]
}
print(d['list'])
# no error by default none set0
print(d.get('li',0))
# [1, 2, 3]
# 0
print(d.keys())
print(d.values())
print(d.items())
# dict_keys(['hello', 'a', 3, 'list'])
# dict_values([1, 20, 14, [1, 2, 3]])
# dict_items([('hello', 1), ('a', 20), (3, 14), ('list', [1, 2, 3])])
for i in d:
    print(i,d[i])
# hello 1
# a 20
# 3 14
# list [1, 2, 3]
for i in d.values():
    print(i)
# 1
# 20
# 14
# [1, 2, 3]
print("hello" in d)
# True