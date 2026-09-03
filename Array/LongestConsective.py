nums=[100,4,200,1,3,2,5]
# n=len(nums)
# max_count=0
# for i in range(n):
#     count=1
#     num=nums[i]
#     while num+1 in nums:
#         count+=1
#         num+=1
#     if max_count<count:
#         max_count=count
# print(max_count)
n=len(nums)
new_set=set()
longest=0
for i in range(n):
    new_set.add(nums[i])
for num in new_set:
    if num-1 not in new_set:
        x=num
        count=1
        while x+1 in new_set:
            count+=1
            x+=1
        if longest<count:
            longest=count
print(longest)

