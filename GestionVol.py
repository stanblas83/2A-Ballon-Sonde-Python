from AllumeCamera import AllumeCamera
from ajouter import ajouter
from retourALaLigne import retourALaLigne
from EteintCamera import EteintCamera
import capteurMPL3115A2
import capteurDHT22
import picamera
from time import sleep

sensorMPL=capteurMPL3115A2.Initialisation()
sensorDHT=capteurDHT22.Initialisation()
camera=picamera.PiCamera()
fichier=open('données.txt','w')
f.write('Pression,Altitude,TemperatureMPL,TemperatureDHT,Humidité')
a2=-1000
a1=capteurMPL3115A2.Altitude(sensorMPL)
sleep(30)
AllumeCamera(camera)

while (a2<0)
  retourALaLigne()
  ajouter(capteurMPL3115A2.Pression(sensorMPL))
	ajouter(a2)
	ajouter(capteurMPL3115A2.Temperature(sensorMPL))
  ajouter(capteurDHT22.Temperature(sensorDHT22))
	ajouter(capteurDHT22.Humidite(sensorDHT22))
  print(capteurMPL3115A2.Temperature(sensorMPL))
  print(capteurDHT22.Temperature(sensorDHT22))
  a2=a2+10
  sleep(5)
EteintCamera(camera)


