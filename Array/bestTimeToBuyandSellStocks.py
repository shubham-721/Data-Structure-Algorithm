prices=[7,1,5,3,6,4,2]
max_profit=0
# for i in range(len(prices)):
#     for j in range(i,len(prices)):
#         profit=prices[j]-prices[i]
#         if max_profit<profit:
#             max_profit=profit
# print(max_profit)
min_price=prices[0]
for price in prices[1:]:
    profit=price-min_price
    if profit>max_profit:
        max_profit=profit
    if price<min_price:
        min_price=price
print(max_profit)