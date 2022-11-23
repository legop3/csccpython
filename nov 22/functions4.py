# functions4.py
# 11/22/2022
# daniel roberts
# shows default parameters

def getRecords(table, field, nrecs):
    allRecs=[]
    for i in range(0,nrecs,1):
        thisRec=[table,field,"record #"+str(i)]
        allRecs.append(thisRec)
    return(allRecs)

records=getRecords("customers","Johnson")
