nums=[7,8,9,1,2,3,4,5,6]
target=1
low=0
n=len(nums)
high=n-1
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]==target:
        print( mid)
        break
    elif nums[low]<=nums[mid]:
        if nums[low]<=target and target<=nums[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        if nums[mid]<=target and target<=nums[high]:
            low=mid+1
        else:
            high=mid-1



