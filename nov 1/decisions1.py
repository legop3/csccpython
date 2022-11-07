# daniel roberts
# 11/1/2022
# decisions.py
# basic python conditionals


# single alternative if test:
ticketPrice=12.00
age=12

if age>55:
    ticketPrice=ticketPrice-(ticketPrice*0.15)
    print("elderly discount applied")


# print("the ticket price is",ticketPrice)


if age<=12:
    ticketPrice-=ticketPrice*0.5
    print("children's discount applied")

print("the ticket price is",ticketPrice)

# double alternative if test:
direction='left'

if direction=='right':
    print("you are driving east")
else:
    print("you are driving west")

# boolean values ******************

flag=True

if flag:
    print("the flag is true")
else:
    print("no, the flag is false")

# three way conditional ************

myInt=0

if myInt<0:
    print("my integer is negative")
elif myInt==0:
    print("my integer is 0")
else:
    print("my integer is positive")







































































































































































# godort