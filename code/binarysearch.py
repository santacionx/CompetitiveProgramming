def binarysearch(li,search):
    s=0
    e=len(li)-1
    while(s<=e):
        mid=(s+e)//2
        if li[mid]==search:
            return mid
        elif search>li[mid]:
            s=mid+1
        else:
            e=mid-1
    
    return -1
search=int(input())
li=[int(i) for i in input().split()]
print(binarysearch(li,search))

