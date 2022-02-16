#!/usr/bin/python3
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from datetime import datetime
import adafruit_dht
import time

dhtDevice = adafruit_dht.DHT11(24)
lcd = LCD()


def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

while True:
    try:
        humidity, temperature = dhtDevice.humidity,dhtDevice.temperature
        now = datetime.now()
        dt_string = now.strftime("%m/%d %a %H:%M")
        lcd.text("{}".format(dt_string), 1)
        if humidity is not None and temperature is not None:   
            lcd.text(("Temp={}  Hmd={}%".format(temperature, humidity)), 2)
            time.sleep(0.4)
    except RuntimeError:
        pass
