def merge(a,b):
    i=0
    j=0
    a1=[]
    while((i<len(a)) and (j<len(b))):
        if(a[i]<b[j]):
            a1.append(a[i])
            i+=1
        else:
            a1.append(b[j])
            j+=1
    while(i<len(a)):
        a1.append(a[i])
        i+=1
    while(j<len(b)):
        a1.append(b[j])
        j+=1
    return a1
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
print(merge(a,b))

