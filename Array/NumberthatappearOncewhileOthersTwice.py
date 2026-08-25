nums=[1,1,2,3,3,4,4,]
for i in range(len(nums)):
    num=nums[i]
    count=0
    for j in range(len(nums)):
        if nums[j]==num:
            count+=1
    if count==1:
        print(num)

