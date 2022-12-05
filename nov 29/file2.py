# file2.py
# 11/29/2022
# daniel roberts
# write an append to file

# f=open('demofile2.txt','a')
# f.write('this is appended text')
# f.write('and this is some more')
# f.close()

f=open('demofile2.txt','w')
f.write('this is new text\n')
f.write('here is some more text\n')
f.write('good luck!')
f.close()
