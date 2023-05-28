# print all words
def prinall(a,k):
    words=a.split()
    d={}
    for i in words:
         d[i]=d.get(i,0)+1
    for i in d:
        if d[i]==k:
             print(i)

a="this is a word string having many word"
k=2
prinall(a,k)
