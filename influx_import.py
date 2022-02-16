from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import Adafruit_DHT
import time
import var.json

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 24

token = ""
org = ""
bucket = "Home-weather"
influx_url=""

while True:
	with InfluxDBClient(url=influx_url, token=token, org=org) as client:
		humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
		write_api = client.write_api(write_options=SYNCHRONOUS)
		if humidity is not None and temperature is not None:
#		print(humidity, temperature)
			data1 = "humidity,room=Bedroom humidity={}".format(humidity)
			data2 = "temperature,room=Bedroom temperature={}".format(temperature)
			write_api.write(bucket, org, data1)
			print("message 1 sent")
			write_api.write(bucket, org, data2)
			print("message 2 sent")
		else:
			time.sleep(1)
			continue
		time.sleep(1)
