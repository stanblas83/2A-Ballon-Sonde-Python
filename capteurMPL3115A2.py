import board
import adafruit_mpl3115a2

def InitailisationMPL3115A2():
  i2c = boardI2C()
  sensor=adafruit_mpl3115a2.MPL3115A2(i2c)
  sensor.sealevel_pressure = 102250
  return sensor

def Altitude(sensor):
  return sensor.altitude

def Pression(sensor):
  return sensor.pressure

def Temperature(sensor):
  return sensor.temperature
