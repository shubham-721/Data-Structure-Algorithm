nums=[1,2,3,4,5,6,8,5,1]
n=len(nums)
# for i in range(n):
#     if (i == 0 or nums[i-1] < nums[i]) and (i == n-1 or nums[i] > nums[i+1]):
#         print(i)
# if n==1:
#     print(0)
# elif nums[0]>nums[1]:
#     print(nums[0])
# elif nums[n-1]>nums[n-2]:
#     print(nums[n-1])
# else:
#     low=0
#     high=n-2
#     while low<=high:
#         mid=low+(high-low)//2
#         if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
#             print(mid)
#             break
#         elif nums[mid]>nums[mid-1]:
#             low=mid+1
#         else:
#             high=mid-1

# shorter version of it
low=0
high=n-1
while low<high:
    mid=low+(high-low)//2
    if nums[mid]<nums[mid+1]:
        low=mid+1
    else:
        high=mid  
print(low)
