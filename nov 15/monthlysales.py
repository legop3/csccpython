# monthlysales.py
# 11/15/2022
# daniel roberts
# demonstrate parallel arrays for month and sales

months=['january','feburary','march','april']
sales=[53849.00,23048.00,34729.00,47157.00]

month=input('for which month do you wish sales?: ')
for i in range(0,len(months),1):
    if months[i]==month:
        print('sales for',months[i],'were',sales[i])