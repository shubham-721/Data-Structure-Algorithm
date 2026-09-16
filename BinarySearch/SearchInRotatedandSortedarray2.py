nums=[7,8,9,1,1,1,2,3,4,5,6]
target=1
n=len(nums)
low=0
high=n-1
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]==target:
        print("element found")
        break
    if nums[low]==nums[mid] and nums[mid]==nums[high]:
        low=low+1
        high=high-1
        continue
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
    
