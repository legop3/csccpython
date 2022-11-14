# spreadsheet.py
# daniel roberts
# 11/8/2022
# resets cells in spreadsheet by row and col

cell=0
for row in range(2,500,1):
    for column in range(4,720,1):
        # print("reset row",row,"column",column)
        print("reset cell",cell,"at row",row,"column",column)
        cell +=1
print("spreadsheet complete")