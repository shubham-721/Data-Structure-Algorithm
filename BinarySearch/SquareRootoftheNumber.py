n=int(input("enter the number"))
if n==0 or n==1:
    print(n)
low=1
high=n//2
ans=1
while low<=high:
    mid=low+(high-low)//2
    if mid* mid <=n:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print(ans)
