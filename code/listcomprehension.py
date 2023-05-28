l=["hello","san","pop","dad"]
# m=[2,3,5,6]
# l1=[ele**2 for ele in l]
# print(l)
# print(l1)
# l2=[ele for ele in l if ele%2==0]
# print(l2)
l3=[[i for i in j] for j in l ]
print(l3)