
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

n=int(input())
r=int(input())
a=factorial(n)
b=factorial(n-r)    
c=factorial(r)
ans=a//(b*c)
print(ans)