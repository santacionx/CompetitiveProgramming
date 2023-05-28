
def check(a,n):
    if(n==0 or n==1):
        return True
    if(a[0]>a[1]):
        return False
    return check(a,n-1)
a=[1,2,3]
n=3
print(check(a,n))