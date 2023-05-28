def swap(li):
    size=len(li)-1
    for i in range(0,size,2):
        temp=li[i]
        li[i]=li[i+1]
        li[i+1]=temp
    return li
li=[int(i) for i in input().split()]
print(swap(li))

