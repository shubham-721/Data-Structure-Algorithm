arr1=[2,4,6,8,10]
arr2=[1,3,6, 8,9,11]
n=len(arr1)
m=len(arr2)
i,j=0,0
result=[]
while i<n and j<m:
    if arr1[i]<arr2[j]:
        i+=1
    elif arr2[j]<arr1[i]:
        j+=1
    else:
        result.append(arr1[i])
        i+=1
        j+=1
print(result)