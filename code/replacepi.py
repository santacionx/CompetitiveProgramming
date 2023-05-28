def rep(s,a,b):
    if len(s)<=1:
        return s
    ans= rep(s[1:],a,b)
    if s[0]=='p' and s[1]=='i':
        return '3.14'+ans
    else:
        return s[0]+ans

s="hepio"
a='l'
b='s'
print(rep(s,a,b))
# hesso 