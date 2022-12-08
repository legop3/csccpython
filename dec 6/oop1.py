# oop1.py
# daniel roberts
# 12/6/2022
# simple classes and object demonstration



class simple:
    x = 5
    y=10
    def sum(self):
        result=self.x+self.y
        return(result)
# create object s1
s1=simple()
print('x in s1 is',s1.x)
s1.x=17
print('the new value of x is',s1.x)
print('s1.y is',s1.y)

# create object s2
s2 = simple()
print('x inside s2',s2.x)
s2.x=-4
print('the new s2.x is',s2.x)
print('s2.y equals',s2.y)


# write and read fields y
s1.y=55
s2.y=300
print('the new ys are',s1.y,s2.y)

# use built in function sum