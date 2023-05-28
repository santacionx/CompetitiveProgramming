# sequence of unicode in vs not in operators:immutable
s="hello world hello"
t="hello to see you"
# list
ans=s.split(' ',2)
print(ans)
# replace
ans=s.replace("hello","san",1)
print(ans)
# find substring index
ans=s.find("hello",1,5)
print(ans)
print(s)
# upper
ans=s.lower()
print(ans)
ans=s.upper()
print(ans)
ans=s.startswith('h',12)
print(ans)