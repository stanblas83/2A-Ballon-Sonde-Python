import adafruit_dht
from board import GPIO4

def Initialisation():
	dht_device = adafruit_dht.DHT22(GPIO4)
  	return dht_device

def Temperature(sensor):
	return str(sensor.temperature)

def Humidite(sensor):
	return str(sensor.humidity)
