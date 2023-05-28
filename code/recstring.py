def rep(s,a,b,n,s1):
    if n<=0:
        return ''+s1
    if s[n-1]==a:
        s1=b+s1
    else:
        s1=s[n-1]+s1
    return rep(s,a,b,n-1,s1)

s="hello"
a='l'
b='s'
print(rep(s,a,b,len(s)," "))