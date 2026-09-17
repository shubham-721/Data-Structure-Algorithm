nums=[1,1,2,3,3,4,4,8,8]
result=0
for num in nums:
    result=result^num
# print(result)

# in (log n)
n=len(nums)
low=0
high=n-1
while low<high:
    mid=low+(high-low)//2
    if mid%2==0:
        if nums[mid]==nums[mid+1]:
            low=mid+2
        else:
            high=mid
    else:
        if nums[mid]==nums[mid-1]:
            low=mid+1
        else:
            high=mid
print(nums[low])

