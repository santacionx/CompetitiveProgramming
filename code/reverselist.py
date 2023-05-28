def reversel(li):
    i=0
    j=len(li)-1
    while(i<j):
        temp=li[i]
        li[i]=li[j]
        li[j]=temp
        i+=1
        j-=1
    return li

li=[int(i) for i in input().split()]
print(reversel(li))

