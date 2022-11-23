# scope.py
# daniel roberts
# 11/22/2022
# shows variable scope in program

def sub_scope():
    varX=22
    print("inside sub scope",varX)

def scope():
    varX=50
    print("inside scope, var x is",varX)
    sub_scope()
    print("after sub scope, var x is",varX)


varX=100
print("in main, var x is",varX)
scope()
print("after scope, var x is",varX)