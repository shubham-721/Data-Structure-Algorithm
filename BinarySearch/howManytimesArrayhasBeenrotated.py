nums=[3,4,5,1,2]
n=len(nums)
low=0
high=n-1
while low<high:
    mid=low+(high-low)//2
    if nums[mid]>nums[high]:
        low=mid+1
    else:
        high=mid
print("Number of rotation of array",low);