nums=[10, 5, 2, 7, 1, 9]
k=int(input("enter the value of K"))
n=len(nums)
max_len=0
prefix_sum=0
mp={}
for i in range(n):
    prefix_sum+=nums[i]
    if prefix_sum==k:
        max_len=i+1
    if prefix_sum-k in mp:
        length=i-mp[prefix_sum-k]
        max_len=max(length,max_len)
    if prefix_sum not in mp:
        mp[prefix_sum]=i
print(max_len)
