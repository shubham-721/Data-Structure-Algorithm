nums = [4, 5, 6, 1, 2, 2, 3]
n=len(nums)
low=0
high=n-1
while low<high:
    mid=low+(high-low)//2
    if nums[mid]>nums[high]:
        low=mid+1
    elif nums[mid]<nums[high]:
        high=mid
    else:
        high=high-1
print("array has been rotated",low);