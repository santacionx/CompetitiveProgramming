
def fi(a,n,x):
    if n<=0:
        return -1
    if(a[n-1]==x):
        return n-1
    return fi(a,n-1,x)
    
a=[1,2,3,-1,-7]
n=len(a)
print(fi(a,n,-7))