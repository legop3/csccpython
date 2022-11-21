name = input('Enter student\'s name: ')
grade1 = input('Enter the 1st test grade: ')
grade2 = input('Enter the 2nd test grade: ')
grade3 = input('Enter the 3rd test grade: ')
sumgrades = float(grade1) + float(grade2) + float(grade3)
average_grade = sumgrades / 3
print('The average test score for', name, 'is', average_grade)
