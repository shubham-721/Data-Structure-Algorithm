l1=[1,2,3,4,5,6]
n=len(l1)
temp=l1[n-1]
for i in range(n-1,0,-1):
    l1[i]=l1[n-1]
l1[0]=temp
print(l1)
