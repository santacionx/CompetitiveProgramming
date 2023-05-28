def binarysearchrec(a,search,s,e):
    if s>e:
        return -1
    mid=(s+e)//2
    if a[mid]==search:
        return mid
    elif search>a[mid]:
        return binarysearchrec(a,search,mid+1,e)
    else:
        return binarysearchrec(a,search,s,mid-1)
    

a=[1,2,3,4,5]
search=5
s=0
e=len(a)
print(binarysearchrec(a,search,s,e))
# hesso 