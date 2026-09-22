piles=[3,6,7,11]
h=8
for k in range(1,max(piles)+1):
    total=0
    for p in piles:
        total+=(p+k-1)//k
    if total<=h:
        print(k)
        break