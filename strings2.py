# Daniel Roberts
# 10/18/2022
# strings2.py
# more output operations

print("we're the so-called \"vikings\" from the north")
print("this is one line\nand this is another")
print("\tthis is\ttabbed\toutput")

str1 = "today is tuesday"
str2 = "programming is fun!"
print("string1 has",len(str1),"characters")
print("string2 has",len(str2),"characters")
print(str1[2])
print(str2[5])

print(" ") #string object functions
str3 = "Hello World!"
print(str3.replace('H','J'))
print(str3)
str3=str3.replace('H','J')
print(str3)