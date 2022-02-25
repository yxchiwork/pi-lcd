from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import adafruit_dht
import time
from dotenv import load_dotenv
import os

load_dotenv()

dhtDevice = adafruit_dht.DHT11(24)

token = os.getenv('influx_token')
org = os.getenv('influxdb_org')
bucket = "Home-weather"
influx_url=os.getenv('influx_url')

while True:
	with InfluxDBClient(url=influx_url, token=token, org=org) as client:
#to update the adadruit read
		humidity, temperature = dhtDevice.humidity,dhtDevice.temperature
		write_api = client.write_api(write_options=SYNCHRONOUS)
		if humidity is not None and temperature is not None:
			data1 = "humidity,room=Bedroom humidity={}".format(humidity)
			data2 = "temperature,room=Bedroom temperature={}".format(temperature)
			write_api.write(bucket, org, data1)
			print(data1)
			write_api.write(bucket, org, data2)
			print(data2)
		else:
			time.sleep(1)
			continue
		time.sleep(1)
