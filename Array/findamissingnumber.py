arr=[1,2,4,5]
n=len(arr)+1
for i in range(1,len(arr)+1):
    n=n^i
    n=n^arr[i-1]
print(n)



