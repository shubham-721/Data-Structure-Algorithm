def countOccurrence(nums,x):
    low=0
    high=len(nums)-1
    first=-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==x:
            first=mid
            high=mid-1
        elif nums[mid]<x:
            low=mid+1
                
        else:
            high=mid-1
    low=0
    high=len(nums)-1
    last=-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==x:
            last=mid
            low=mid+1
        elif nums[mid]>x:
            high=mid-1
        else:
            low=mid+1
    if first==-1:
        return 0
    return last-first+1
nums = [1, 2, 2, 2, 3, 4]
print(countOccurrence(nums, 1))
