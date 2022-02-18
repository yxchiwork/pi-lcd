# What is this?
This is my home hobby project with Raspberry Pi (Zero 2W, and 4B (4GB/8GB)), I'm using DHT11 sensor to grab the temperature and humidity data from my rooms then send them to InfluxDB cloud. Grafana then will pick up the data from InfluxDB and visualize it. 

# What's in here? 
- LCD display module with reading data using adafruit-circuitpython-dht package. 
- Linux service file to run the LCD module at Pi boot.
- Sending data to InfluxDB Cloud instance.

# Ansible (still learning)
- Currently I'm building an ansible playbook to deploy the code and enable services to Pis.
