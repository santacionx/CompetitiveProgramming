
def sumr(a,n):
    if(n==0):
        return 0
    return sumr(a,n-1)+a[n-1]
a=[1,2,3]
n=len(a)
print(sumr(a,n))