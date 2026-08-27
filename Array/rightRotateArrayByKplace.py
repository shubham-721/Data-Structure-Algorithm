nums=[1,2,3,4,5,6,7]
k=int(input("enter the element"))
n=len(nums)
k=k%n
left=0
right=n-1
while left<right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
left=0
right=k-1
while left<right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
left=k
right=n-1
while left<right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
print(nums)


