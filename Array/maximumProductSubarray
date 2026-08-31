nums = [2, 3, -2, 4]
max_product=nums[0]
min_product=nums[0]
ans=nums[0]
for i in range(len(nums)):
    x=nums[i]
    if x<0:
        temp=max_product
        max_product=min_product
        min_product=temp
    if max_product*x>x:
        max_product=max_product*x
    else:
        max_product=x
    if min_product*x<x:
        min_product=min_product*x
    else:
        min_product=x
    if max_product>ans:
        ans=max_product
print(ans)