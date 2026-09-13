def lowerBound(nums,target,n):
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
nums=[3,5,8,15,19,19,19]
n=len(nums)
print(lowerBound(nums,9,n))