from time import sleep
from AllumeCamera import AllumeCamera
from retourALaLigne import retourALaLigne
from ajouter import ajouter
from EteintCamera import EteintCamera
import picamera
import board
import adafruit_mpl3115a2
import capteurMPL3115A2

camera=picamera.PiCamera()
AllumeCamera(camera)
sensorMPL3115A2 = InitialisationMPL3115A2()

f = open ( 'donnees.txt' , 'w' )
f.write  ( 'Temperature,Altitude,Pression,' )
f.close()
n=0
h=0
while n<=5 : 
	retourALaLigne()
	sleep( 5 )
	ajouter(capteurMPL3115A2.Temperature(sensorMPL3115A2))
	ajouter(capteurMPL3115A2.Altitude(sensorMPL3115A2))
  ajouter(capteurMPL3115A2.Pression(sensorMPL3115A2))
	n=n+1

EteintCamera(camera)
MP4Box -add my_video.h264 video.mp4
