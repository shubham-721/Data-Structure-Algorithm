nums=[1,2,3]
# we have to find the  subarray sum equal k
n=len(nums)
k=int(input("enter the number "))
# count=0
# for i in range(n):
#     sum=0
#     for j in range(i,n):
#         sum=sum+nums[j]
#         if sum==k:
#             count+=1        
# print(count)
dic={}
max_len=0
sum=0
for i in range(n):
    sum+=nums[i]
    if sum==k:
        if max_len<i+i:
            max_len=i+i
    rem=sum-k
    if rem in dic:
        len=i-dic[rem]
        if max_len<len:
            max_len=len
    if sum not in dic:
        dic[sum]=i
# print(max_len)
left=0
summ=0
maxlen=0
for right in range(n):
    summ+=nums[right]
    while summ>k:
        summ-=nums[left]
        left+=1
    if summ ==k:
        length=right-left+1
        if maxlen<length:
            maxlen=length
print(maxlen)
