nums=[2,4,5,8,9,10]
target=19
# n=len(nums)
# for num in range(n-1):
#     for num2 in range(1,n):
#         if nums[num]+nums[num2]==target:
#             print(num,num2)
# using dicitonary
dicc = {}
i = 0
for num in nums:
    req = target - num
    if req in dicc:
        print("Index:", dicc[req], i)
        print("Number:", req, num)
        break
    dicc[num] = i
    i += 1
