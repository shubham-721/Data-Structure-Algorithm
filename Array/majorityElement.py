nums=[2,2,1,1,1,2,2,1,1]
n=len(nums)
# for num in nums:
#     count=0
#     for num2 in nums:
#         if num==num2:
#             count+=1
# if count>n/2:
#     print(num)
count={}
for num in nums:
    if num in count: 
        count[num]=count[num]+1
    else:
        count[num]=1
for num in count:
    count[num]=n/2
print(num)