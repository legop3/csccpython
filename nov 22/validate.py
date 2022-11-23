# daniel roberts
# validate.py
# 11/22/22
# this does simple validation of user input ensuring that it is integer (integer check)

test_str=input("what is your integer? ")
while not test_str.isdigit():
    test_str=input("please enter integer: ")
number=int(test_str)
print("test string is",number)