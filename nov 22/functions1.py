# daniel roberts
# 11/22/2022
# functions1.py
# basic python functions

import time

def greet():
    print("hello world")

def getDay():
    now=time.time()
    # print("now is",now)
    tStruct=time.localtime(now)
    # print("t structure",tStruct)
    today=time.strftime("%m/%d/%Y",tStruct)
    return(today)

def getTime():
    now=time.time()
    # print("seconds from epoch",now)
    tStruct=time.localtime(now)
    # print("t structure",tStruct)
    clockTime=(str(tStruct.tm_hour)+ ":" + 
               str(tStruct.tm_min)+ ":"+ 
               str(tStruct.tm_sec))
    return(clockTime)

# main program ********************

print("now starting main program")
greet()
print("just called greet")

print("today is",getDay())
print("right now is",getTime())
time.sleep(2.3)
print("and now the time is",getTime())
time.sleep(1.7)
print("finally, the time is",getTime())