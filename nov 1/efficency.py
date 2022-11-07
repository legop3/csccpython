# daniel roberts
# efficency.py
# 11/1/2022
# tricks to optimize conditionals

scoreTxt=int(input("what is the score? "))


# the worse way would be to convert to int every time

# better way
if scoreTxt>=90:
    print('it is A')
elif scoreTxt>=80:
    print('it is B')
elif scoreTxt>=70:
    print('it is c')
elif scoreTxt>=60:
    print('it is D')
else:
    print('it is E')

