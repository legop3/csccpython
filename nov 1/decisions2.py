# daniel roberts
# decisions2.py
# 1/11/2022
# more python conditional ops

userName="Daniel"
password="cscc"

if userName=="Daniel" and password=="cscc":
    print("welcome, user!")
else:
    print("sorry, not recognized")

# or operator **********************

leftDoor='open'
rightDoor='closed'

if leftDoor=='open' or rightDoor=='open':
    print('sound the door buzzer')
else:
    print('turn off buzzer')


# combination of and and or **********
if (3<4 or 7>6) and 8==4:
    print("it is true")
else:
    print("no it is not")