import adafruit_dht
from board import <pin>

def InitialisationDHT22(pin):
  dht_device = adafruit_dht.DHT22(<pin>)
  return dht_device

def Temperature(sensor):
  return sensor.temperature

def Humidite(sensor):
  return sensor.humidity
