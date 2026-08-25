l1=[1,1,1,2,2,4,5,6,6]
n=len(l1)
i=0
j=i+1
while j<n:
    if l1[j]!=l1[i]:
        i+=1
        l1[i],l1[j]=l1[j],l1[i]
    j+=1
# print(i+1)
print(l1[:i+1])
    
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)
# n=len(l1)
# freq_map={}
# for i in range(1,n):
#     freq_map[l1[i]]=0
# j=0
# for k in freq_map:
#     l1[j]=k
#     j+=1
# print(j)

