#!/bin/bash

sudo cp -f /home/robot/EWeekCode/Gamepad/pf_mecanum_gamepad.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable pf_mecanum_gamepad.service
sudo systemctl start pf_mecanum_gamepad.service