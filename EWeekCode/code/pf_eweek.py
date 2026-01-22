import time
import Board as Board

def MotorStop(): # stop all motors 
    Board.setMotor(1, 0) 
    Board.setMotor(2, 0)
    Board.setMotor(3, 0)
    Board.setMotor(4, 0)

def Forward(speed, secs):
    '''
    Moves the robot forward
    
    :param int speed: the speed of the motor
    :param int secs: the time (s) the motors will move
    '''
    Board.setMotor(1, speed, secs) 
    Board.setMotor(2, speed, secs)
    Board.setMotor(3, speed, secs)
    Board.setMotor(4, speed, secs)
    time.sleep(secs)    # This keeps the robot moving for 1 second
    MotorStop()         # This stops all motors

def Reverse(speed, secs):
    '''
    Moves the robot in reverse
    
    :param int speed: the speed of the motor
    :param int secs: the time (s) the motors will move
    '''
    # TODO Set the the individual motors speed and direction to
    # HINT: You will need to set all 4 motors

    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    MotorStop()         # This stops all motors

def TurnRight(speed, secs):
    '''
    Turns the robot to the right
    
    :param int speed: the speed of the motor
    :param int secs: the time (s) the motors will move
    '''
    # TODO Set the the individual motors speed and direction to
    # HINT: You will need to set all 4 motors

    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    MotorStop()         # This stops all motors

def TurnLeft(speed, secs):
    '''
    Turns the robot to the left
    
    :param int speed: the speed of the motor
    :param int secs: the time (s) the motors will move
    '''
    # TODO Set the the individual motors speed and direction to
    # HINT: You will need to set all 4 motors

    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    MotorStop()         # This stops all motors

def StrafeRight(speed, secs):
    '''
    Strafes the robot to the right
    
    :param int speed: the speed of the motor
    :param int secs: the time (s) the motors will move
    '''
    # TODO Set the the individual motors speed and direction to
    # HINT: You will need to set all 4 motors

    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    MotorStop()         # This stops all motors

def StrafeLeft(speed, secs):
    '''
    Strafes robot to the left
    
    :param int speed: the speed of the motor
    :param int secs: the time (s) the motors will move
    '''
    # TODO Set the the individual motors speed and direction to
    # HINT: You will need to set all 4 motors

    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    MotorStop()         # This stops all motors

def DiagonalLeft(speed, secs):
    '''
    Moves the robot diagonally to the left
    
    :param int speed: the speed of the motor
    :param int secs: the time (s) the motors will move
    '''
    # TODO Set the the individual motors speed and direction to
    # HINT: You will need to set all 4 motors

    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    MotorStop()         # This stops all motors

def DiagonalRight(speed, secs):
    '''
    Moves the robot diagonally to the right
    
    :param int speed: the speed of the motor
    :param int secs: the time (s) the motors will move
    '''
    # TODO Set the the individual motors speed and direction to
    # HINT: You will need to set all 4 motors

    # Don't modify below
    time.sleep(secs)    # This keeps the robot moving for x amount of secs
    MotorStop()         # This stops all motors

if __name__ == '__main__':
    speed = 40                  # Sets the speed of the motors
    secs = 1                    # Seconds each function will run
    Forward(speed, secs)        # This makes the robot move forward with speed set to 40 for 1 second
    # TODO Call each function here to test your code!
    