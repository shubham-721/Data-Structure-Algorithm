nums=[10, 5, 2, 7, 1, 9]
k=int(input("enter the value of K"))
n=len(nums)
# max_len=0
# prefix_sum=0
# mp={}
# for i in range(n):
#     prefix_sum+=nums[i]
#     if prefix_sum==k:
#         max_len=i+1
#     if prefix_sum-k in mp:
#         length=i-mp[prefix_sum-k]
#         max_len=max(length,max_len)
#     if prefix_sum not in mp:
#         mp[prefix_sum]=i
# print(max_len)
length=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=nums[j]
        if (sum==k):
            current_len=j-i+1
            if current_len>length:
                length=current_len
print(length)
