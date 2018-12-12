# -*- coding: utf-8 -*-
"""
Module for exiting program
"""
import sys
# check for 'quit' or 'exit'
def checkExit(v):
    ## check if the user input 'x' or 'quit'
    print("Content for checking to quit the app")
    if v == "X":
        print("\n\n")
        print("##########################################################\n")
        print("Thank you for playing. Good Bye!")
        sys.exit()
    else:
        return True
