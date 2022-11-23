# functions2.py
# daniel roberts
# 11/22/2022
# show arguments and parameters for functions

def greet(firstName, lastName):
    print("hello,",firstName,lastName)

def calcPayCheck(wages):
    federalTaxRate=0.23
    stateTaxRate=0.08

    grossPay=wages/26.0
    fedTax=grossPay*federalTaxRate
    stateTax=grossPay*stateTaxRate
    netPay=grossPay-fedTax-stateTax
    netPay=round(netPay,2)
    return(netPay)

def callByValue(parm):
    parm=123
    print("inside function, parm is",parm)
    return(parm)

# main program ***************

greet("lisa","simpson")
greet("michael","jordan")
greet("peter","gabriel")

mySalary=68000.00
myPayCheck=calcPayCheck(mySalary)
print("my paycheck is",myPayCheck)

print("stan's paycheck is",calcPayCheck(66000.00))
print("sue's paycheck is",calcPayCheck(72000))

myArg=99
print("before calling function is",myArg)

