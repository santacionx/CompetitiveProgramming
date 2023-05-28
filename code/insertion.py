def ins(li):
    length=len(li)
    for i in range(1,length):
      temp=li[i]
      j=i-1
      while(j>=0):
          if li[j]>temp:
              li[j+1]=li[j]
          j-=1
      li[j+1]=temp
     
    return li
li=[int(i) for i in input().split()]
print(ins(li))

