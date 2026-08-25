arr1=[1,2,3,4,5,5,6]
arr2=[1,1,2,3,4,5,6,7]
n=len(arr1)
m=len(arr2)
i=0
j=0
Union=[]
while i<n and j<m:
    if arr1[i]<arr2[j]:
        if not Union or Union[-1]!=arr1[i]:
            Union.append(arr1[i])
        i+=1
    elif arr1[i]>arr2[j]:
        if not Union or Union[-1]!=arr2[j]:
            Union.append(arr2[j])
        j+=1
    else:
        if not Union or Union[-1]!=arr1[i]:
            Union.append(arr1[i])
        i+=1
        j+=1
while i<n:
    if not Union or Union[-1]!=arr1[i]:
        Union.append(arr1[i])
    i+=1
while j<m:
    if not Union or Union[-1]!=arr2[j]:
        Union.append(arr2[j])
    j+=1
print(Union)
    
