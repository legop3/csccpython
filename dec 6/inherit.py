# inherit.py
# daniel roberts
# 12/6/2022
# basic inheritence in python

class Item:
    def __init__(self, name, sku, price):
        self.name=name
        self.sku=sku
        self.price=price

    def __str__ (self):
        iStr = "item name " + self.name + ', '
        iStr = iStr + 'skoo ' + str(self.sku) + ', '
        iStr = iStr + 'Retail Price $' + str(self.price)
        return(iStr)

class Clothes (Item):
    def __init__(self, name, sku, price, size):
        super().__init__(name, sku, price)
        self.size=size

class TShirt(Clothes):
    def __init__(self, name, sku, price, size, fit):
        super().__init__(name, sku, price, size)
        self.fit=fit
    
    def __str__(self):
        iStr = "item name " + self.name + ', '
        iStr = iStr + 'skoo ' + str(self.sku) + ', '
        iStr = iStr + 'Retail Price $' + str(self.price) + ', '
        iStr = iStr + 'Size ' + str(self.size) + ', '
        iStr = iStr + 'Fit ' + self.fit
        
        return(iStr)


item01=Item("parasol", 4354, 10.99)
print(item01.__str__())

item02=Clothes("formal shoes",4873, 45.00, 7)
print('item02',item02.name, item02.size)
print(item02.__str__())

item03=TShirt('casual shirt',4398,25.35,10,'relaxed')
print(item03.__str__())