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
## import json/csv
## import requests
## import api 
## import math

#----variable declaration----#

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
    
# check for 'quit' or 'exit'
def checkExit(v):
    ## check if the user input 'x' or 'quit'
    print("Content for checking to quit the app")
    if v.capitalize() == "X":
        print("\n\n")
        print("##########################################################\n")
        print("Thank you for playing. Good Bye!")
        sys.exit()
    else:
        return True

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
    
    print("Your recommended calorie intake should be {} calories.".format(rCalorie))
        
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
                  'C' and activityInput):
            raise ValueError
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

# set activity level
# turn activityInput convert into uppercase and strip whitespace
    
## get valid user name

## get valid user gender
uGender = input("Enter 1 for Female or 2 for Male or 3 for other: ")    

## ---get valid user weight
uWeight = input("How much do you weigh?: ")
 
## ---get valid user age
uAge = input("Age: ")

## --get valid user height
# validate input - can be inches or feet and inches
uHeight = input("Enter your height: ")

## display recommended calorie intake based on the demographic data
rCalories(uAge, uGender, uHeight, uWeight)

#---------get valid user meal information------------#
## get valid meal type
## get main course (list choices collected from the api data load)
## get the side course (list choices collected from the api data load)
## get the drink (list choices collected from the api data load)
## get the dessert (list choices collected from the api data load)
## calculate and display calorie intake
## calculate and display how much more or less calories the user consumes
thankyouMessage()
