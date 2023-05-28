n=int(input())
i=1
l=1
while(i<=n):
    j=1
    while(j<=i):
        print(j,end=" ")
        j+=1
    # 2*n-2 even spaces in between
    s=2*n-2
    while(s>=1):
        print(' ',end='')
        s-=1
    k=i
    while(k>=1):
        print(k,end=" ")
        k-=1
    print()
    i+=1
