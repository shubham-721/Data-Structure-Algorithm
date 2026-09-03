nums=[3,9,50,15,99,7,98,65]
n=len(nums)
max=nums[0]
min=nums[0]
for i in range(n):
    if nums[i]>max:
        max=nums[i]
    if min>nums[i]:
        min=nums[i]
print(min,max)

