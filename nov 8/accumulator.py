# accumulator.py
# daniel roberts
# demonstrates value that accumulates
# 11/8/2022

totalPrice=0.00

itemPrice=float(input("Enter price first item (0 to end): "))
while itemPrice >0.0:
    totalPrice+=itemPrice
    print("total is", totalPrice)
    itemPrice=float(input("what is next item? (0 to end): "))
print("total price is", totalPrice)