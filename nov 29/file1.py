# file1.py
# 11/29/2022
# daniel roberts
# read from existing file

# f=open('./demofile.txt','r')
# print(f.read())

"""
f=open('demofile.txt','rt')
print('<',f.readline(),'>')
print('<',f.readline(),'>')
print('<',f.readline(),'>')
print('<',f.readline(),'>')
f.close()
"""
"""
f=open('demofile.txt','r')
print(f.read(5))
print(f.read(7))
print(f.read(3))
f.close()"""

f=open('demofile.txt','rt')
for record in f:
    print(record)
f.close()