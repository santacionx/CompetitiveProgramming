s=input().split()
n,m=int(s[0]),int(s[0])
b=input().split()
li=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
print(li)