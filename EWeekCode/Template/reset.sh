#!/bin/bash

sudo systemctl stop pf_mecanum_gamepad.service
cp -f /home/robot/EWeekCode/Template/Control.py  /home/robot/EWeekCode/Template/Model.py /home/robot/EWeekCode/code