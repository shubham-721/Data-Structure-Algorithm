nums=[3,1,-2,-5,2,-4]
# n=len(nums)
# i=0
# j=1
# while i<n and j<n:
#     if nums[i]>0:
#         i+=2
#     elif nums[j]<0:
#         j+=2
#     else:
#         nums[i],nums[j]=nums[j],nums[i]
#         i+=2
#         j+=2
# print(nums)
pos=[0]*3
neg=[]
p=0
for num in nums:
    if num >0:
        # pos.append(num)
        pos[p]=num
        p+=1
    else:
        neg.append(num)
for i in range(len(pos)):
    nums[2 * i] = pos[i]
    nums[2 * i + 1] = neg[i]
print(nums)


