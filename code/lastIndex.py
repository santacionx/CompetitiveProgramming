
def fi(a,n,x):
    if n<=0:
        return -1
    ans= fi(a,n-1,x)
    if(a[n-1]==x):
        return n-1
    return ans
a=[1,2,1,1,-7]
n=len(a)
print(fi(a,n,1))