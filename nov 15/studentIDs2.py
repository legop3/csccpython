# studentIDs2.py
# 11/15/2022
# daniel roberts
# student IDs using list properties

studentIDs=[]

id=int(input('what is first id? (0 to end): '))
while id !=0:
    studentIDs.append(id)

    id=int(input('enter the next ID (0 to end): '))
print('student IDs are',studentIDs)

studentIDs.pop()
studentIDs.pop()

print('trimmed IDs are',studentIDs)