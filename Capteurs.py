import Adafruit_DHT
import smbus
import time

sensor = Adafruit_DHT.DHT22
pin = 4

def DHT22():
    [humidity, temperature] = Adafruit_DHT.read_retry(sensor, pin)
    return([humidity, temperature])

