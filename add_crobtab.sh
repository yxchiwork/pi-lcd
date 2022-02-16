#!/bin/bash

line1="5 20 * * * python3 /home/pi/lcd_light_off.py"
line2="0 20 * * * systemctl stop lcd"
line3="0 8 * * * systemctl restart lcd"

(crontab -u pi -l; echo "$line1" ) | crontab -u pi -
(crontab -u root -l; echo "$line2" ) | crontab -u root -
(crontab -u root -l; echo "$line3" ) | crontab -u root -