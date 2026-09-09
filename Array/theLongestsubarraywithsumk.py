nums=[10, 5, 2, 7, 1, 9]
k=int(input("enter the value of K"))
n=len(nums)
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=nums[j]
        if (sum==k):
            current_len=j-i+1
            if current_len>length:
                length=current_len
print(length)
