def first_Occurence(nums,x):
    low=0
    high=len(nums)-1
    ans=-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==x:
            ans=mid
            high=mid-1
        elif nums[mid]<x:
            low=mid+1   
        else:
            high=mid-1
    return ans
def last_occurence(nums,x):
    low=0
    high=len(nums)-1
    ans=-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==x:
            ans=mid
            low=mid+1
        elif nums[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return ans
nums=[2,4,6,8,8,8,11,13]
x=11
print(first_Occurence(nums,x))
print(last_occurence(nums,x))