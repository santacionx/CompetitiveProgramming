
def cn(a,n,x):
    if(n<0):
        return False
    if(a[n-1]==x):
        return True
    return cn(a,n-1,x)
a=[1,2,3,-1,-7]
n=len(a)
print(cn(a,n,-2))