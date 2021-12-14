from time import sleep
from ajouter import ajouter
from retourALaLigne import retourALaLigne
import capteurMPL3115A2
import picamera
from AllumeCamera import AllumeCamera
from EteintCamera import EteintCamera

sensor=capteurMPL3115A2.Initialisation()
camera=picamera.PiCamera()
f = open ( 'donnees.txt' , 'w' )
f.write  ( 'Pression,Altitude,Temperature,' )
f.close()
n=0

AllumeCamera(camera)

while n<5 : 
	retourALaLigne()
	ajouter(capteurMPL3115A2.Pression(sensor))
	ajouter(capteurMPL3115A2.Altitude(sensor))
	ajouter(capteurMPL3115A2.Temperature(sensor))
	sleep(2)
	n=n+1

EteintCamera(camera)
