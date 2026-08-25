nums=[12,42,45,3,5,2,9]
target=9
n=len(nums)
for i in range(1,n):
    if nums[i]==target:
        print(i)
print(-1)