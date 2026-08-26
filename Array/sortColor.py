nums=[0,2,2,1,1,0,1,2,0,2,1,2,1,0]
# count0=0
# count1=0
# count2=0
# for i in nums:
#     if i==0:
#         count0+=1
#     elif i==1: 
#         count1+=1
#     elif i==2:
#         count2+=1
# for i in range(count0):
#     nums[i]=0
# for i in range(count0,count0+count1):
#     nums[i]=1
# for i in range(count0+count1,len(nums)):
#     nums[i]=2
# print(nums)
low=0
mid=0
high=len(nums)-1
while mid<=high:
    if nums[mid]==0:
        nums[low],nums[mid]=nums[mid],nums[low]
        low+=1
        mid+=1
    elif nums[mid]==1:
        mid+=1
    else:
        nums[mid],nums[high]=nums[high],nums[mid]
        high-=1
print(nums)

