def bubble(li):
    length=len(li)
    for i in range(length):
      mini=i
      for j in range(0,length-i-1):
          if li[j]>li[j+1]:
             li[j],li[j+1]=li[j+1],li[j]
     
    return li
li=[int(i) for i in input().split()]
print(bubble(li))

