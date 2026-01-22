# E-Week PathFinderBot Robotics Workshop


Empowering Engineers Through Hands-On Robotics and Leadership Development

Welcome to the PathfinderBot repository! This project provides engineers and technical teams with a hands-on robotics and leadership development experience. Participants will assemble, program, and operate the MasterPi robot, applying both technical and strategic skills to complete challenges.

![Workshop Setup](./zzimages/2025Setup500Robot.jpg)

## Installation
***Instructors Only*** 
1. Click on the green Code dropdown button on Github and download as a zip
2. Transfer file to the Robot's Pi (USB, scp from external machine, or Browser on Robot's Pi)
3. unzip it under /home/robot
4. Run the following
```bash
mv /home/robot/eweekpathfinderbot/EWeekCode /home/robot/
rm -rf eweekpathfinderbot
rm -f eweekpathfinderbot.zip
```
5. You should have all the files under /home/robot/EWeekCode on completition


# Workshop Phases

1. Coding Challenge
- learn about Python functions, docstrings, conditional statements, loops, and more!
- implement functions to perform tasks such as driving forward, sonar detection, and picking up blocks
- learn about the model-view-controller pattern

2. Course Challenge
- Navigate a course with obstacles and blocks
- leverage a wireless gamepad to drive the robot and pick up blocks



# Coding Instructions
***For Students***
1. You will be coding in one file ***Model.py***
2. You will only need to write code under the ***TODO*** sections
3. On the left side bar, click on Remote Explorer
4. Click on the robot host EWeekCode folder (may just be an IP address) and click connect in current Window. The password is R4spb3rry.
5. In the code folder, you should open up the ***Control.py*** and ***Model.py*** files
6. Start coding!
7. To test your code, open a terminal by click Terminal -> New Terminal in the top bar of Visual Studio Code
8. Run the following in the terminal to run your code (Password is R4spb3rry)

```bash
cd /home/EWeekCode/code
sudo python Control.py 
```
9. If you get stuck, go ahead and open the Answers folder to see what you're missing!

## Reset Code
If you want to restart your code, run the following to reset the code to the original assignment

```bash
sudo /home/robot/EWeekCode/Template/reset.sh
```

# Wireless Gamepad Service
***Instructors Only***

To start the gamepad service to enable wireless Logitech Gamepad control of the robot, run the following

```bash
sudo /home/robot/EWeeCode/Gamepad/gamepad_setup.sh
```

## Gamepad Controls
**Note**: the left stick may be the D-Pad depending on the controller and X and Y may be swapped.

- **Left stick Y**:   RIGHT-side track forward/back (swapped)
- **Right stick Y:**  LEFT-side track forward/back (swapped)
- **Left/Right X**:   mecanum strafe left/right (average of both X axes)
- **Right trigger:**  analog drive forward (both sides)
- **Left trigger:**   analog drive backward (both sides)
- **Right bumper:**  turn right in place
- **Left bumper:**    turn left in place

Actions
- **A button:**      look_forward (arm/camera pose)
- **B button:**       look_sad (expression)
- **X button:**       say_no
- **Y button:**       say_yes
- **Logitech button:** look_around
- **D-pad UP:****     pickup_block
- **D-pad DOWN:**     backward_drop_block
- **D-pad LEFT:**     left_pickup_block
- **D-pad RIGHT:**    right_pickup_block
- **Back button:**    all-stop (motors off)
- **Start button:**   quit program


## Reference
This code is fork of https://github.com/stemoutreach/PathfinderBot