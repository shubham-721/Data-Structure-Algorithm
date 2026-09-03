nums=[16,17,4,3,5,2]
# output=[17,5,2]
result=[]
for i in range(len(nums)):
    leader=True
    for j in range(i+1,len(nums)):
        if nums[j]>nums[i]:
            leader=False
            break
    if (leader==True):
        result.append(nums[i])
print(result)

        