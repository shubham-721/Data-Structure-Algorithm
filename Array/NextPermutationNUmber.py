nums=[1,2,3]
pivot=-1
n=len(nums)
# finding the pivot element the condition of pivot element is nums[i]<nums[i+1]
for i in range(n-2,-1,-1):
    if nums[i]<nums[i+1]:
        pivot=i
        break
if pivot==-1:
    left=0
    right=n-1
    while left<right:  #inplace swapping a number
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
# print(nums)
else:
    left=pivot+1
    right=n-1
    # finding the next greater element to pivot element
    for i in range(n-1,pivot,-1):
        if nums[i]>nums[pivot]:
            nums[i],nums[pivot]=nums[pivot],nums[i]
            break
    # reverse all the element next to pivot
    i=pivot+1
    j=n-1
    while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
print(nums)
            