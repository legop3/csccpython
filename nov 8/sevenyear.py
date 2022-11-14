# sevenyear.py
# daniel roberts
# 11/8/2022
# two versions of the seven day sale

itemPrice=47.95
discount=0.07

for day in range(1,8,1):
    itemPrice-=itemPrice*discount
    itemPrice=round(itemPrice,2)
    print("on day",day,"item is",itemPrice)
print("sale complete")