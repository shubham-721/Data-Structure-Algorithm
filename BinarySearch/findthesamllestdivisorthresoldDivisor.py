nums=[1,2,5,9]
t=6
# output=5
low=1
high=max(nums)
while low<=high:
    mid=low+(high-low)//2
    div=0
    for d in nums:
        div=div+(d+mid-1)//mid
    if div<=t:
        high=mid-1
    else:
        low=mid+1
print(low)

    