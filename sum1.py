def hello(n):
    if n==0:
        return 0
    return n+hello(n-1);

n=int(input())
print(hello(n))