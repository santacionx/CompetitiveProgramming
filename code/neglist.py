
li=[1,2,3,"hello"]
# list stores references when operation used creates a new li and copies

for i in li[-4:]:
    print(i,end=" ")
print()
for i in li[0::2]:
    print(i,end=" ")