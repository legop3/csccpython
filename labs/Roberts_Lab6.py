# Roberts_Lab6.py
# 12/1/2022
# Daniel Roberts
# Programming fundamentals lab 6, BMI calculations and tables. takes user's data and runs BMI and Karvonen calculations on it.


# functions:


# BMI formula, takes weight in kilograms and height in meters
def bmi(weight, height):
    bmi=(weight/(height**2))
    
    return(bmi)

# print(bmi(75, 1.75))



# karvonen formula, takes age in years, resting heart rate in BPM and intensity in percentage (like '55' means 55%)
def karvonen(age, restingHR, intensity):
    intensity=intensity/100
    out=(((220-age)-restingHR)*intensity)+restingHR
    return(out)

# print(karvonen(60, 60, 55))

# user's data entry, check that they enter only numbers.
print("Please enter the following values for the user . . .")

height = input("height in inches: ")
while not height.isdigit():
    height = input("height in inches: ")

weight = input("Weight in pounds: ")
while not weight.isdigit():
    weight = input("Weight in pounds: ")


age = input("age in years: ")
while not age.isdigit():
    age = input("age in years: ")

restingHR = input("resting heart rate in BPM: ")
while not restingHR.isdigit():
    restingHR = input("resting heart in BPM: ")



# convert height and weight from imperial to metric
height    = float(height) * 0.0254
weight    = float(weight) / 2.205
age       = float(age)
restingHR = float(restingHR)
# print("converted weight and height")
# print(weight)
# print(height)



print("Results . . .")
bmiOut = round(bmi(weight, height), 2)


# generate text to classify BMI
# bmiOut=float(input("enter bmi for testing: "))
if bmiOut<18.5:
    bmiString = "Underweight"
if bmiOut >18.5 and bmiOut<24.9:
    bmiString = "Normal weight"
if bmiOut >=25 and bmiOut<29.9:
    bmiString = "Overweight"
if bmiOut > 30:
    bmiString = "Obese"

print("Your BMI is:",bmiOut,"--",bmiString)

print("\nExercise Intensity Heart Rates:")
print("Intensity\t Max Heart Rate\n")
for intensity in range(50,100,5):
    print("{intensity}%\t\t".format(intensity=intensity), round(karvonen(age, restingHR, intensity)))