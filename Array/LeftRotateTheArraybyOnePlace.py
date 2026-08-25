l1=[1,2,3,4,5,6]
temp=l1[0]
n=len(l1)
for i in range(1,n):
    l1[i-1]=l1[i]
l1[n-1]=temp
print(l1)