"""
This file is the Model for the project.
This manages business logic for the robot.

You will implement the functions listed as TODO.
Once you implement a function, run the Control.py code on your robot to test it!
"""

##################################################################
# DO NOT MODIFY FUNCTIONS WITHOUT A TODO
##################################################################
import time
import Board as Board
from Sonar import Sonar as Sonar

def motorStop():
    """
    Stops all 4 motors
    """
    Board.setMotor(1, 0) 
    Board.setMotor(2, 0)
    Board.setMotor(3, 0)
    Board.setMotor(4, 0)

# This is an example to move the motors
def forward(speed, secs):
    """
    Moves the robot forward
    
    :param int speed: the speed of the motor
    :param int secs: the duraction (s) the motors will move
    """
    Board.setMotor(1, speed)    # this sets motor 1 to the specified speed
    Board.setMotor(2, speed)
    Board.setMotor(3, speed)
    Board.setMotor(4, speed)

    time.sleep(secs)            # This keeps the robot moving for x amount of secs
    motorStop()                 # This stops all motors

##################################################################
# TODO TASKS BEGIN HERE. YOU MAY MODIFY TODO FUNCTIONS BELOW
##################################################################

def reverse(speed, secs):
    """
    Moves the robot in reverse
    
    :param int speed: the speed of the motor
    :param int secs: the duraction (s) the motors will move
    """
    # TODO Task 1: Set the the individual motors speed and direction to move in reverse
    # HINT: You will need to set all 4 motors
    Board.setMotor(1, -speed) 
    Board.setMotor(2, -speed)
    Board.setMotor(3, -speed)
    Board.setMotor(4, -speed)
    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    motorStop()         # This stops all motors

def turnRight(speed, secs):
    """
    Turns the robot to the right
    
    :param int speed: the speed of the motor
    :param int secs: the duraction (s) the motors will move
    """
    # TODO Task 2: Set the the individual motors speed and direction to turn right
    # HINT: You will need to set all 4 motors
    Board.setMotor(1, speed) 
    Board.setMotor(2, -speed)
    Board.setMotor(3, speed)
    Board.setMotor(4, -speed)
    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    motorStop()         # This stops all motors

def turnLeft(speed, secs):
    """
    Turns the robot to the left
    
    :param int speed: the speed of the motor
    :param int secs: the duraction (s) the motors will move
    """
    # TODO Task 3: Set the the individual motors speed and direction to turn left
    # HINT: You will need to set all 4 motors
    Board.setMotor(1, -speed) 
    Board.setMotor(2, speed)
    Board.setMotor(3, -speed)
    Board.setMotor(4, speed)
    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    motorStop()         # This stops all motors

def strafeRight(speed, secs):
    """
    Strafes the robot to the right
    
    :param int speed: the speed of the motor
    :param int secs: the duraction (s) the motors will move
    """
    # TODO Task 4: Set the the individual motors speed and direction to strafe right
    # HINT: Think about the direction the motors spin
    Board.setMotor(1, speed) 
    Board.setMotor(2, -speed)
    Board.setMotor(3, -speed)
    Board.setMotor(4, speed)
    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    motorStop()         # This stops all motors

def strafeLeft(speed, secs):
    """
    Strafes robot to the left
    
    :param int speed: the speed of the motor
    :param int secs: the duraction (s) the motors will move
    """
    # TODO Task 5: Set the the individual motors speed and direction to strafe left
    # HINT: Think about the direction the motors spin 
    Board.setMotor(1, -speed) 
    Board.setMotor(2, speed)
    Board.setMotor(3, speed)
    Board.setMotor(4, -speed)
    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    motorStop()         # This stops all motors

def sonarDetection():
    """
    Changes LED colors based on Sonar Distances
    """
    startTime = time.time()         # Gets the start time (current time)
    duration = 5                   # duration in seconds
    sonar = Sonar()                 # creates a Sonar object
    sonar.setRGBMode(0)             

    redColor = Board.PixelColor(255, 0, 0)      # Red Color
    greenColor = Board.PixelColor(0, 255, 0)    # Green Color 
    blueColor = Board.PixelColor(0, 0, 255)     # Blue is default
    color = blueColor 

    while time.time() - startTime < duration:   # Loops for 30 seconds
        distance = sonar.getDistance()          # Gets distance from sensor in mm
        print(f"Distance: {distance} mm")       # Prints distance to terminal output

        # Don't modify above
        # TODO Task 6: write an if-else statement to set the color based on distance
        # - If distance is less than 200 (mm), set the color to red. Otherwise, set it to green
        # HINT: set color equal to the redColor or greenColor above
        if distance < 200:
            color = redColor
        else:
            color = greenColor
        # Don't modify below
        sonar.setPixelColor(0, color)           # Set LED 0 to the color
        sonar.setPixelColor(1, color)           # Set LED 1 to the color
        sonar.show()                            # Show the LED colors

        time.sleep(0.5)                         # Wait half a second before looping again

# This is an example of turning the servos
def look_forward():
    """
    Resets Arm Position to Forward
    """
    Board.setPWMServoPulse(1, 1500, 500)
    Board.setPWMServoPulse(3, 700, 1000)
    Board.setPWMServoPulse(4, 2425, 1000)
    Board.setPWMServoPulse(5, 790, 1000)
    Board.setPWMServoPulse(6, 1500, 1000)
    time.sleep(1)

# This is an example of turning the servos
def turnArmLeft():
    """
    Turns Robot arm to the left
    """
    Board.setPWMServoPulse(1, 2020, 1000)
    Board.setPWMServoPulse(3, 800, 1000)
    Board.setPWMServoPulse(4, 2020, 1000)
    Board.setPWMServoPulse(5, 2091, 1000)
    Board.setPWMServoPulse(6, 2500, 1000)
    time.sleep(1)
    look_forward()


def turnArmRight():
    """
    Turns Robot arm to the right
    """
    # TODO Task 7: Set the servos to turn the arm to the right
    # HINT: Board.setPWMServoPulse(servo_id, pulse, use_time)
    # - Servo number (1–6)
    # - pulse: Position (typically between 500 and 2500)
    # - use_time: Time in milliseconds to move
    Board.setPWMServoPulse(1, 2020, 1000)
    Board.setPWMServoPulse(3, 800, 1000)
    Board.setPWMServoPulse(4, 1800, 1000)
    Board.setPWMServoPulse(5, 2091, 1000)
    Board.setPWMServoPulse(6, 500, 1000)
    # Don't modify below
    time.sleep(1)
    look_forward()

def openAndCloseClaw():
    """
    Opens and closes arm claw
    """
    # TODO Task 8: Set the servos to open and close the claw
    # HINT: Board.setPWMServoPulse(servo_id, pulse, use_time)
    # - Servo number (1–6)
    # - pulse: Position (typically between 500 and 2500)
    # - use_time: Time in milliseconds to move
    Board.setPWMServoPulse(3, 900, 800)
    Board.setPWMServoPulse(5, 2364, 800)
    Board.setPWMServoPulse(1, 2020, 2000)
    # Don't modify below
    time.sleep(1)
    look_forward()
    
##################################################################
# BONUS TASKS
##################################################################

def diagonalLeft(speed, secs):
    """
    Moves the robot diagonally to the left
    
    :param int speed: the speed of the motor
    :param int secs: the duraction (s) the motors will move
    """
    # TODO Bonus Task 1: Set the the individual motors speed and direction to
    # HINT: You will need to set 2 motors
    Board.setMotor(1, speed) 
    Board.setMotor(4, speed)
    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    motorStop()         # This stops all motors

def diagonalRight(speed, secs):
    """
    Moves the robot diagonally to the right
    
    :param int speed: the speed of the motor
    :param int secs: the duraction (s) the motors will move
    """
    # TODO Bonus Task 2: Set the the individual motors speed and direction to
    # HINT: You will need to set 2 motors
    Board.setMotor(2, speed) 
    Board.setMotor(3, speed)
    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    motorStop()         # This stops all motors

def pickupBlock():
    """
    Robot arm picks up the block in front of it
    """
    # TODO Bonus Task 3: Implement a sequence of arm movements to pickup a block in 
    # front of the robot
    Board.setPWMServoPulse(1, 1500, 2000)
    Board.setPWMServoPulse(3, 590, 2000)
    Board.setPWMServoPulse(4, 2500, 2000)
    Board.setPWMServoPulse(5, 700, 2000)
    Board.setPWMServoPulse(6, 1500, 2000)

    Board.setPWMServoPulse(5, 1818, 1000)
    time.sleep(1)
    Board.setPWMServoPulse(4, 2023, 300)
    Board.setPWMServoPulse(5, 2091, 300)
    time.sleep(0.3)
    Board.setPWMServoPulse(1, 1932, 400)
    time.sleep(0.4)
    Board.setPWMServoPulse(3, 750, 800)
    Board.setPWMServoPulse(5, 2364, 800)
    time.sleep(0.8)
    Board.setPWMServoPulse(1, 1455, 300)
    Board.setPWMServoPulse(5, 2318, 300)
    time.sleep(0.3)
    Board.setPWMServoPulse(5, 1841, 1000)
    time.sleep(1)
    look_forward()