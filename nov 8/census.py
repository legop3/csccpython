# daniel roberts
# 11/8/2022
# census.py

for year in range(1970,2040,10):
    print("census scheduled for",year)
print("census complete")
print("")

# now use the modulus
for year in range(1974, 2037):
    # print(year)
    # print("modulus", year % 10)
    if (year%10==0):
        print(year, "is a census year")
print("census complete")