x=int(input("enter the number"))
m=int(input("enter the power"))
low=1
high=x
result=-1
while low<=high:
    mid=low+(high-low)//2
    ans= mid**m
    if ans==x:
        result=mid
        break
    elif ans<x:
        low=mid+1
    else:
        high=mid-1
print(result)