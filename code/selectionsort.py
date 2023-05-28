def selectionsort(li):
    length=len(li)
    for i in range(length):
      mini=i
      for j in range(i+1,length):
          if li[j]<li[mini]:
            mini=j
      li[i],li[mini]=li[mini],li[i]
    return li
li=[int(i) for i in input().split()]
print(selectionsort(li))

