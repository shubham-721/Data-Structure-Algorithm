nums=[1, 2, 4, 6, 8]
x=5
n=len(nums)
floor=-1
ceil=-1
low=0
high=n-1
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]==x:
        floor = nums[mid]
        ceil = nums[mid]
        break
    elif nums[mid]<x:
        low=mid+1
        floor=nums[mid]
    else:
        high=mid-1
        ceil=nums[mid]
print(floor)  
print(ceil)