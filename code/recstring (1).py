def rep(s,a,b):
    if len(s)<=0:
        return s
    ans= rep(s[1:],a,b)
    if s[0]==a:
        return b+ans
    else:
        return s[0]+ans

s="hello"
a='l'
b='s'
print(rep(s,a,b))
# hesso 