nums=[16,17,4,3,5,2]
# output=[17,5,2]
# result=[]
# for i in range(len(nums)):
#     leader=True
#     for j in range(i+1,len(nums)):
#         if nums[j]>nums[i]:
#             leader=False
#             break
#     if (leader==True):
#         result.append(nums[i])
# print(result)
n=len(nums)
result=[nums[n-1]]
maxi=nums[n-1]
for i in range(n-2,-1,-1):
    if maxi<nums[i]:
        maxi=nums[i]
        result.append(maxi)
# print(result)
n=len(result)
i=0
j=n-1
while i<j:
    result[i],result[j]=result[j],result[i]
    i+=1
    j-=1
print(result)
