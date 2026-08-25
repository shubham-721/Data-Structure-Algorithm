l1=[1,2,3,5,6,6]
for i in range(1,len(l1)):
    if l1[i-1]>l1[i]:
        print(False)
        break
else:
    print(True)
