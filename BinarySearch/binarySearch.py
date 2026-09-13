def binarySearch(nums,n,target):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif target>nums[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
nums=[3,4,6,7,9,12,16,17]
n=len(nums)
print(binarySearch(nums,n,target=13))           