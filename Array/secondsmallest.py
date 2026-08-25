l1=[23,43,634,523,632,623]
smallest=l1[0]
secondSmallest=float("-inf")
for i in l1:
    if i <smallest:
        smallest=i
    elif i<secondSmallest and secondSmallest!=smallest:
        secondSmallest=i
print(secondSmallest)

# this program is with going with error
