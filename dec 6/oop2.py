# oop2.py
# daniel roberts
# 12/6/2022
# object oriented programming 2, demonstrates constructor functions

class simple:
    def __init__(self, x, y):
        self.x = x
        self.y = y


s1 = simple(14, 67)
print('s1s values',s1.x,s1.y)

s2 = simple(4324, 14354523)
print('s2 values',s2.y,s2.x)