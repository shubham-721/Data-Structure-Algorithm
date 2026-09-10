nums=[1,2,3,-3,1,1,1,1,4,2,-3]
k=int(input("enter the value of k"))
count=0
n=len(nums)
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=nums[j]
        if sum==k:
            count+=1
# print(count)
dic={0:1}
count=0
prev_sum=0
for i in range(n):
    prev_sum+=nums[i]
    prefix_sum=prev_sum-k
    if prefix_sum in dic:
        count+=dic[prefix_sum]
    if prev_sum in dic:
        dic[prev_sum]+=1
    else:
        dic[prev_sum]=1
print(count)