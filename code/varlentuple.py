def sum1(a,b, *more):
    ans=a+b
    for i in more:
        ans+=i
    print(ans)
def sd(a,b):
    return a+b,a-b
sum1(1,2,3)
d,e=sd(1,2)
print(d,e)