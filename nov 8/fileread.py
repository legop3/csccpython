# fileread.py
# daniel roberts
# 11/8/2022
# simulate reading file record by record

record=input("What is first record? ")
while record!="eof":
    print("record is",record)
    record=input("enter next record (eof to end): ")
print("file read")