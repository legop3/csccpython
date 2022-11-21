# employee.py
# daniel roberts
# 11/15/2022
# using lists as non-typed arrays

emp1=[25565,'john doe','marketing',85000.00,'27 mar 2013']
print('employee\'s id is',emp1[0])
print('employee\'s department is',emp1[2])
print('employee\'s salary is',emp1[3])

# two dimensional arrays!
employees=[]
employees.append(emp1)

print('employees is',employees)

emp2=[43421,'susan smith','IT',92000.00,'19 nov 2005']
emp3=[43623,'carlos roe','sales',72000.00,'03 july 2009']
employees.append(emp2)
employees.append(emp3)

# print('employees are now',employees)

for employee in employees:
    print(employee)

print('susan\'s hire date', employees[2][4])