# daniel roberts
# 11/15/2022
# arrays1.py
# using lists as basic arrays

salaries = [48000.00, 72400.00, 66800.00, 3900.00, 54800.00]
print(salaries[1])
print(salaries[4])
print('salaries are', salaries)
print("")

print('salaries has', len(salaries),'elements')
for i in range(len(salaries)):
    print('salary',i,'is',salaries[i])

print('')
i=1
for salary in salaries:
    print('salary',i,'is',salary)
    i+=1

# this will error
# print('salary[5]', salaries[5])
salaries[2] = 4800.00
print('new salaries',salaries)