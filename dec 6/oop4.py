# oop4.py
# daniel roberts
# 12/6/2022
# show getters and setters

class Address:
    def __init__(self, street, city):
        self.street=street
        self.city=city

class PrivateAddress:
    def __init__(self, street, city):
        self.__street=street
        self.__city=city

    def getStreet(self):
        return(self.__street)
    
    def getCity(self):
        return(self.__city)

    def setStreet(self, street):
        self.__street=street
    
    def setCity(self, city):
        self.__city=city

# main program------------------------

joes_place=Address('22 maple', 'delaware')
print('joes street',joes_place.street)
print('joes city',joes_place.city)

car_shop=PrivateAddress('777 granite way','bryce')
print('car shops street',car_shop.getStreet())
print('car shops city',car_shop.getCity())

car_shop.setStreet('432 noble lane')
print('car shops new street is',car_shop.getStreet())