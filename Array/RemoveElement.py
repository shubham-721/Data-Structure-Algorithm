nums=[2,2,4,2,3,5,2,5,3,0]
val=3
n=len(nums)
k=0
for i in range(n):
    if nums[i]!=val:
        nums[k]=nums[i]
        k+=1
print(nums[:k])