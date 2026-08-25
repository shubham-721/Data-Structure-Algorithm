arr=[1,1,0,1,1,1,0,1,1,1,1]
count=0
maxCount=0
for i in range(len(arr)):
    if arr[i]==1:
        count+=1
        if maxCount<count:
            maxCount=count
    elif arr[i]!=1:
        count=0
        continue
print(maxCount)
    