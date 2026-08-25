arr=[1,3,0,4,2,34,5,0,0,9,12]
n=len(arr)
left=0
# for right in range(n):
#     if arr[right]!=0:
#         arr[left],arr[right]=arr[right],arr[left]
#         left+=1
# print(arr)
right=0
while right<n:
    if arr[right]!=0:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
    right+=1
    
print(arr)
print(arr)
