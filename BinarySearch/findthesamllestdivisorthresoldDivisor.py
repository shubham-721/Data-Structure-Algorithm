nums=[1,2,5,9]
t=6
result=0
# output=5
large=0
for i in range(len(nums)):
    if nums[i]>large:
        large=nums[i]
print(large)
for i in range(1,large+1):
    total=0
    