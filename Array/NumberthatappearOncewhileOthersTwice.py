nums=[1,1,2,3,3,4,4,]
# for i in range(len(nums)):
#     num=nums[i]
#     count=0
#     for j in range(len(nums)):
#         if nums[j]==num:
#             count+=1
#     if count==1:
#         print(num)

result=0
for num in nums:
    result^=num
print(result)

# using dicitionary

dic={}
for num in nums:
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
for num in dic:
    if num==1:
        print(num)

