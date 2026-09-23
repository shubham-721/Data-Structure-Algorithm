piles=[3,6,7,11]
h=8
for k in range(1,max(piles)+1):
    total=0
    for p in piles:
        total=total+(p+k-1)//k
    if total<=h:
        # print(k)
        break
low=1
high=max(piles)
# ans=float("inf")
while low<=high:
    mid=low+(high-low)//2
    totalhours=0
    for p in piles:
        totalhours=totalhours+(p+mid-1)//mid
    if totalhours<=h:
        # ans=mid
        high=mid-1
    else:
        low=mid+1
print(low)
