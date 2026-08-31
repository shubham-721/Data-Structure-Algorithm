nums=[12,-4,3,23,52,-2,53,5,-4]
max_sum=nums[0]
# for i in range(len(nums)):
#     sum=0
#     for j in range(i,len(nums)):
#         sum=sum+nums[j]
#         if sum>max_sum:   
#             max_sum=sum
# print(max_sum)
sum=0
ansStart=0
ansEnd=0
start=0
for i in range(len(nums)):
    if sum==0:
        start=i
    sum=sum+nums[i]
    if sum>max_sum:
        max_sum=sum
        ansStart=start
        ansEnd=i
    if sum<0:
        sum=0
print(max_sum)
print(ansStart,ansEnd)

