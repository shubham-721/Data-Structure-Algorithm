# def binarySearch(nums,n,target):
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]==target:
#             return mid
#         elif target>nums[mid]:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# nums=[3,4,6,7,9,12,16,17]
# n=len(nums)
# print(binarySearch(nums,n,target=13))     
#  Recursive approach
def BS(nums,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif target>nums[mid]:
       return BS(nums,mid+1,high,target)
    else:
        return BS(nums,low,mid-1,target)
nums=[3,4,6,7,9,12,16,17]
n=len(nums)
low=0
high=n-1
print(BS(nums,low,high,target=12))
