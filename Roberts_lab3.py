# roberts_lab3.py
# 10/24/2022
# printing invoices and calculations.
# Daniel Roberts

# define variables
books = 52.99
labFees = 25.00
tuition = 157.93*3

print("*"*50)

# print out the school's address
print("\tColumbus State Community College")
print("\t550 East Spring Street")
print("\tColumbus, Ohio  43215")

print("-"*50)

# print out the fees individually
print("\tProduct Name:\tProduct Price")
print("\tBooks\t\t$"+str(books))
print("\tLab Fees\t$"+str(labFees))
print("\tTuition\t\t$"+str(tuition))

print("-"*50)

# print out the total
print("\t\t\tTotal")
print("\t\t\t$ "+str(books+tuition+labFees))

print("-"*50)

# print the thank you note and the end of the invoice
print("\n   Thank you for being a Columbus State Student")
print("*"*50)