# oop3.py
# daniel roberts
# 12/6/2022
# more constructor functions

class employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def calcPayCheck(self):
        grossPay=self.salary/26.0
        tax=0.34
        netPay=grossPay-(grossPay*tax)
        netPay=round(netPay,2)
        return(netPay)

fred = employee("fred flinstone", 48000.00)
print('freds full name', fred.name)
print('freds yearly wages',fred.salary)
print('freds paycheck is', fred.calcPayCheck())

barney = employee('barney rubble', 50000.00)
print('barneys full name',barney.name)
print('barneys yearly wages',barney.salary)
print('barneys pay check is',barney.calcPayCheck())