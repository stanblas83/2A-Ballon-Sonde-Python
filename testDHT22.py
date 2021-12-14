from time import sleep
from ajouter import ajouter
from retourALaLigne import retourALaLigne
import capteurDHT22
import picamera
from AllumeCamera import AllumeCamera
from EteintCamera import EteintCamera

sensor=capteurDHT22.Initialisation()
camera=picamera.PiCamera()
f = open ( 'donnees.txt' , 'w' )
f.write  ( 'Temperature,Humidite,' )
f.close()
n=0

AllumeCamera(camera)

while n<5 : 
	retourALaLigne()
	ajouter(capteurDHT22.Temperature(sensor))
	ajouter(capteurDHT22.Humidite(sensor))
	sleep(2)
	n=n+1

EteintCamera(camera)
