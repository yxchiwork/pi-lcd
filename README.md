# What is this?
This is my home hobby project with Raspberry Pi (Zero 2W, and 4B (4GB/8GB)), I'm using DHT11 sensor to grab the temperature and humidity data from my rooms then send them to InfluxDB cloud. Grafana then will pick up the data from InfluxDB and visualize it. 

# What's in here? 
- LCD display module with reading data using adafruit-circuitpython-dht package. 
- Linux service file to run the LCD module at Pi boot.
- Sending data to InfluxDB Cloud instance.
- Crontab jobs to stop the LCD display at night, then re-enable it in the morning.
- influx_env_sample.sh file for /etc/profile.d/, this will set the permanent environment variable in the system. 

# Ansible (still learning)
- main file is completed, apt and pip packages will be installed, this repo will be also cloned.
- pending 5 tasks to expend it to multi-file, functions.

# Known issue
- ada_fruit_dht package doesn't work on 2 processes at the same time. I will have to use the legacy package at the same time. 