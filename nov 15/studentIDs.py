# studentIDs.py
# daniel roberts
# 11/15/2022
# reading input to write in array

studentIDs=[0,0,0,0]

for i in range(0,len(studentIDs),1):
    id=int(input('enter student ID: '))
    studentIDs[i]=id
print('student ids are',studentIDs)