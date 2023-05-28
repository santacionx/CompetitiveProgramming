# sequence of unicode in vs not in operators:immutable
def replacechar(s,a,b):
    s1=""
    for i in s:
        if i==a:
            s1=s1+b
        else:
            s1=s1+i
    return s1

s="hello"
a='l'
b='s'
print(replacechar(s,a,b))