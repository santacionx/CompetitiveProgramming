def linear(li):
    for i in range(len(li)):
      if search==li[i]:
        return i
    return -1


search=int(input())
li=[int(i) for i in input().split()]
print(linear(li))

