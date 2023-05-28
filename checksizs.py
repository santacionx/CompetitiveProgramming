def sbs(a,n):
    if n==0:
        return True;
    if a[0]>a[1]:
        return False
    return(a,n-1)

a=[1,2,3,4,5]
n=len(a)
print(sbs(a,n))