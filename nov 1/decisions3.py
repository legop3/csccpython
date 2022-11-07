# daniel roberts
# decisions3.py
# 11/1/2022
# more conditional stuff

string1='This is MP4'
string2='This is mp4'

if string1.upper()==string2.upper():
    print("they are equal")
else:
    print('they are not')


# floats and equality
myFloat=1.2-1.0

if myFloat==0.2:
    print('yes it is 0.2')
else:
    print('no it is not 0.2')
    print('it is really',myFloat)

# the correct way of doing floats
if myFloat>=0.199 and myFloat<=0.211:
    print('yes, it is near 0.2')
else:
    print('no it is not')

# range functions
nItems=14

if nItems<=3:
    print('no discount')
elif nItems<=8:
    print('discount is 7.5%')
elif nItems<=15:
    print('discount is 12%')
else:
    print('discount is 15%')

# the wrong way
if nItems<=3:
    print('no discount')
elif nItems<=8:
    print('discount is 7.5%')
elif nItems<=15:
    print('discount is 12%')
elif nItems>15:
    print('discount is 15%')
else:
    print('this is dead code')