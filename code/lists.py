
li=[1,2,3,"hello"]
# list stores references when operation used creates a new li and copies
for i in range(len(li)):
    print(li[i],end=" ")
print()
for i in range(2,len(li)):
    print(li[i],end=" ")
print()
for i in li:
    print(i,end=" ")
print()
for i in li[0:3]:
    print(i,end=" ")