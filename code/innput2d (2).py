s=input().split()
n,m=int(s[0]),int(s[0])
b=s[2:]
li=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
print(li)