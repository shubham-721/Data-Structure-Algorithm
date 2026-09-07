nums=[1,2,3]
# we have to find the  subarray sum equal k
n=len(nums)
k=int(input("enter the number "))
count=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum=sum+nums[j]
        if sum==k:
            count+=1        
print(count)
