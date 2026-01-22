"""
This file is the Control class for the project. 

This class is the entrance to the program
"""

from Model import *

if __name__ == '__main__':
    speed = 40                  # Sets the speed of the motors
    secs = 1                    # Seconds each function will run
    forward(speed, secs)        # This makes the robot move forward with speed set to 40 for 1 second

    ################################
    # Motor Controls
    ################################

    # You may commnent (place # in front of) any function to isolate your tests of each function! 
    reverse(speed, secs)              # Task 1
    turnLeft(speed, secs)             # Task 2
    turnRight(speed, secs)            # Task 3
    strafeLeft(speed, secs)           # Task 4 
    strafeRight(speed, secs)          # Task 5

    ################################
    # Sonar Controls
    ################################
    sonarDetection()                  # Task 6

    ################################
    # Arm Controls
    ################################
    turnArmRight()                   
    turnArmLeft()                     # Task 7
    openAndCloseClaw()                # Task 8

    ################################
    # Bonus Tasks
    ################################
    diagonalLeft(speed, secs)         # Bonus Task 1
    diagonalRight(speed, secs)        # Bonus Task 2
    pickupBlock()                     # Bonus Task 3
 