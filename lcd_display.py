#!/usr/bin/python3
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from datetime import datetime
import Adafruit_DHT
#import adafruit_dht
import time

# uncomment this if you want to use new package.
#dhtDevice = adafruit_dht.DHT11(24)
lcd = LCD()
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 24

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

while True:
    try:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        now = datetime.now()
        dt_string = now.strftime("%m/%d %a %H:%M")
        lcd.text("{}".format(dt_string), 1)
        if humidity is not None and temperature is not None:   
            lcd.text(("Temp={0:0.0f}  Hmd={1:0.0f}%".format(temperature, humidity)), 2)
            time.sleep(30)
    except RuntimeError:
        pass
