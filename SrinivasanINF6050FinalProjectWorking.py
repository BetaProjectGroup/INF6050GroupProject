# !/usr/bin/env python3  
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 00:28:28 2018

@author: Sushila Srinivasan
Course: INF6050 Intro to Computer Programming
School: School of Information Science, Wayne State University
Assignment: Final Group Project
"""   
#----import modules required----#
import sys
from checkExit import checkExit
## import requests
## import api 
## import math

# API call


#----variable declaration----#

v = 'X'

## username
uName = ''

## age
uAge = 0

## gender
uGender = ''

## height
uHeight = 0

## weight
uWeight = 0

## activity level
uSedentary = 1.2
uLightActivity = 1.375
uModerateActivity = 1.55
uVeryActive = 1.725
uExtraActive = 1.9
activityLevel = 0
level = 0

## recommended calorie
rCalorie = 0

## meal details
mealType =  ['breakfast', 'lunch', 'dinner']

#--- user defined functions ------#

# welcome message
def welcomeMessage():
    ## welcome message content
    print("\nWelcome Message\n")
    
# user instruction
def userInstructions():
    ## user instructions content
    print("\nUser Instructions\n")
    print("Type X to exit")

# validate number
def isNum(v):
    ## check if the user input a valid number
    print("Input is/not a valid number")
    if v.isdigit():
        if int(v)<100:
           return True
        else:
           return False
    else:
        return False
    
# thank you message does not return value or takes argument
def thankyouMessage():
    ## print thank you message
    print("\nThank you for trying the game/app!\n")
    
# calculate recommended calories
def rCalories(uAge, uGender, uHeight, uWeight):
    ## add calorie calculation info based on the demographic data
    print("\n\nYour recommended calories\n")
    if uGender == "1":
        bmrFemale = 655.0 + (4.35 * float(uWeight)) + (4.7 * float(uHeight)) - (4.7 * float(uAge))
        rCalorie = bmrFemale * activityLevel
    elif uGender == "2":
        bmrMale = 66 + (6.23 * float(uWeight)) + (12.7 * float(uHeight)) - (6.8 * float(uHeight))
        rCalorie = bmrMale * activityLevel
    elif uGender == "3":
        rCalorie = 2
    # Truncate rcalorie so that it returns calorie intake to 2 decimal places
    print("Your recommended calorie intake should be {} calories.".format(round(rCalorie, 2)))
        
# calculate meal intake calories
def mCalories(mainDish, sideDish, drink, dessert, mealType):
    ## use the argument values and calculate calorie intake
    print("Your current calorie intake")
    
# print activity levels
def activityLevels():
    print("Please choose your current activity level based:\n"+
          "A for sedentary\nB for lightly active\n"+ 
          "C for moderately active\nD for very active\nE for Extra active\n")

# set activity leve
def setActivity(aInput):
    if aInput == "A":
        level = 1.2
    elif aInput == "B":
        level = 1.375
    elif aInput == "C":
        level = 1.55
    elif aInput == "D":
        level = 1.725
    elif aInput == "E": 
        level = 1.9
    else:
        level = 1
        
    return level

#--------------------begin main program---------------------#
welcomeMessage()
userInstructions()

#---------get valid user demographic information------------#
## get valid user activity level
activityLevels()
def activityInputFunc():
    activityInput = input("Please input your activity level(A/B/C/D/E): \n")
    activityInput = activityInput.strip().upper()
    
# Validate input by checking if input is blank, or a character other than
# a, b, c, d, or e
# check if input is blank
    try:
        if not activityInput:
            raise ValueError
        # check if input is a character other than a, b, c, d, e
        elif (activityInput != 'A' and activityInput != 'B' and activityInput != 
                  'C' and activityInput and activityInput != 'D'
                  and activityInput != 'E' and activityInput != 'X'):
            raise ValueError
        elif activityInput == "X":
            checkExit(v)
        else:
            return activityInput
            
    except ValueError:
        print("You must enter A, B C, D, or E. You entered: '" 
              + activityInput + "'")

        # clear out variable's value
        activityInput = None
    
        # Call activityInputFunc() again
        return activityInputFunc()
    
aInput = activityInputFunc()
activityLevel = setActivity(aInput)

## Valid gender input
while True:
    gInputs = [1,2,3]
    uGender = input("Enter 1 for Female or 2 for Male or 3 for other: ")
    try:
        i = int(uGender)
        if i in gInputs:
            break
        else:
            raise ValueError
    except:
        if uGender.strip().upper() == "X":
            checkExit(v)

## ---get valid user weight
while True:
    uWeight = input("How much do you weigh? (Please round to the nearest whole "
                " number): ")
    try:
        val = int(uWeight)
        if val > 0:
            break
        else:
            print("Please enter a whole number.")
            raise ValueError
    except ValueError:
        if uWeight.strip().upper() == "X":
            checkExit(v)
    
## ---get valid user age
while True:
    try:
        uAge = input("Please enter your age: ")
        if int(uAge) > 0 and int(uAge) < 120:
            break
        else:
            print("Please enter a valid age.")
            raise ValueError
    except:
        if uAge.strip().upper() == "X":
            checkExit(v)

## --get valid user height
# validate input - can be inches or feet and inches
print("")
print("Enter your height.")
while True:
    heightFt = input("Enter feet: ")
    try:
        valFt = int(heightFt)
        if valFt > 0:
            break
        else:
            print("Please enter a whole number.")
            raise ValueError
    except ValueError:
        if heightFt.strip().upper() == "X":
            checkExit(v)
    
while True:
    heightIn = input("Enter inches: ")
    try:
        valIn = int(heightIn)
        if valIn > 0:
            break
        else:
            print("Please enter a whole number.")
            raise ValueError
    except ValueError:
        if heightIn.strip().upper() == "X":
            checkExit(v)       
        
# convert feet and inches to only inches
uHeight = (int(heightFt) * 12) + int(heightIn)
    
print("You entered", heightFt + "ft", heightIn + "in")


## display recommended calorie intake based on the demographic data
rCalories(uAge, uGender, uHeight, uWeight)

#---------get valid user meal information------------#
## get valid meal type

## get main course (list choices collected from the api data load)

mainDish = input("Enter your entree or the main source of protein in your meal. "
                 "For example, chicken, tofu, beef or fish: ")
if mainDish == "X":
    checkExit(v)

sideDish1 = input("Enter your first side dish. For example, potatoes, "
                  " or corn: ")
if sideDish1 == "X":
    checkExit(v)
    
sideDish2 = input("Enter your second side dish. For example, rice, pasta, "
                  " or bread: ")
if sideDish2 == "X":
    checkExit(v)
# match meal input with calories
# convert strings to ints

# Calculate meal total
calcMeal = mainDish + sideDish1 + sideDish2 
## calculate and display calorie intake
print("The calorie intake for your meal is: ")
## calculate and display how much more or less calories the user consumes
calBalance = rCalories - calcMeal

print("You have", calBalance + " remaining today.")

thankyouMessage()
