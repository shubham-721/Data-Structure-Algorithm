l1=[31,45,42,53,542,63,23,342]
largest=secondlargest=0;
for i in l1:
    if i>largest:
        largest=i
    elif i>secondlargest and secondlargest!=largest:
        secondlargest=i
print(secondlargest)
