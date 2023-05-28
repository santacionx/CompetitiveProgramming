search=int(input())
li=[int(i) for i in input().split()]
found=False
for i in range(len(li)):
    if search==li[i]:
        print(i)
        found=True       
        break
if found is False:
    print("not found")

