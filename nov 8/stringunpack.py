# stringunpack.py
# daniel roberts
# 11/8/2022
# string unpacking 
# in definite loop

myString=input("please enter string: ")

print(len(myString))

for ichr in range(0,len(myString),1):
    print("Character",ichr,"is",myString[ichr])
print("unpack complete")

# j