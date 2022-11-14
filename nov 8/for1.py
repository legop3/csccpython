# for1.py
# 11/8/22
# daniel roberts
# some basic for loop structures

for i in range(10):
    print("i equals", i)

print("out of loop")

# for with start and range
for i in range(4,10):
    print("i is now",i)
    print("this is the second loop")
print("second loop complete")
print(" ")

# for with start, end, and step
for i in range(3,25,4):
    print("third loop, i is",i)
print("third loop complete\n")

# for with negative incriments
for i in range(10,0,-1):
    print("fourth loop, i is",i)
print("BLASTOFF!!")