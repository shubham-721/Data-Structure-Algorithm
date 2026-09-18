nums = [1,3,5,6]
target = 5
# output=2
n=len(nums)
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
print(ans)



