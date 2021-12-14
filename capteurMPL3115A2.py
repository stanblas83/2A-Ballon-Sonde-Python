import board
import adafruit_mpl3115a2

def Initialisation():
	i2c=board.I2C()
	sensor=adafruit_mpl3115a2.MPL3115A2(i2c)
	sensor.sealevel_pressure=102250
	return sensor

def Altitude(sensor):
	return str(sensor.altitude)

def Pression(sensor):
	return str(sensor.pressure)

def Temperature(sensor):
	return str(sensor.temperature)
