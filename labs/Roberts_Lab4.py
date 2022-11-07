# lab4.py
# Daniel Roberts
# 11/7/2022
# lab 4 for intro to programming, simple calculator that can add/subtract/multiply/divide


# the inputs, ask for the user's operation, and their two numbers.
operation = input("Please select one option: add/subtract/multiply/divide: ")
firstNumber = float(input("What is the first number? "))
secondNumber = float(input("What is the second number? "))

# figure out which operation the user wants to do and calculate, tell user if they entered an invalid operation.
if operation == 'add':
    print(firstNumber, '+', secondNumber, '=', firstNumber+secondNumber)
elif operation == 'subtract':
    print(firstNumber, '-', secondNumber, '=', firstNumber-secondNumber)
elif operation == 'multiply':
    print(firstNumber, '*', secondNumber, '=', firstNumber*secondNumber)
elif operation == 'divide':
    print(firstNumber, '/', secondNumber, '=', firstNumber/secondNumber)
else:
    print('The option you chose (' + operation + ') is not valid.\nPlease try the program again.')