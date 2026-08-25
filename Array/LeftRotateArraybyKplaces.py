nums=[1,2,3,4,5,6,7,8]
# n=len(nums)
# k=int(input("enter the element"))
# if n!=0:
#     k=k%n
#     temp=nums[:k]
#     for i in range(k,n):
#         nums[i-k]=nums[i]
#     for i in range(k):
#         nums[n-k+i]=temp[i]
#     print(nums)
# USING TWO POIINTER APPROACH
n=len(nums)
k=int(input("enter the element"))
if n!=0:
    k=k%n
    left=0
    right=k-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    # print(nums)
    left=k
    right=n-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    # print(nums)
    left=0
    right=n-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    print(nums)

