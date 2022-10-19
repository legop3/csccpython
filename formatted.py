# 10/18/2022
# daniel roberts
# formatted.py
# built in text formatting

txt = "today is {temp} degrees."
print(txt)
print(txt.format(temp=40))

myPrice=49.95702
txt="for ${price:.2f} today only!"
print(txt.format(price=myPrice))