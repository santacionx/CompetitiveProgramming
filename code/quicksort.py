def part(a,s,e):
    val=a[s]
    count=0
    for i in range(s,e+1):
        if a[i]<val:
           count=count+1
    
    a[s+count],a[s]=a[s],a[s+count]
    pindex=s+count
    i=s
    j=e
    while(i<j):
        if a[i]<val:
            i+=1
        elif a[j]>val:
            j-=1
        else:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    return pindex

def quicksort(a,s,e):
    if(s>=e):
      return
    pindex=part(a,s,e)
    quicksort(a,s,pindex-1)
    quicksort(a,pindex+1,e)

a=[10,9,8,7,5,3,2,1]
quicksort(a,0,len(a)-1)
print(a)