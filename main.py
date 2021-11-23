from time import sleep
from AllumeCamera import AllumeCamera
from retourALaLigne import retourALaLigne
from ajouter import ajouter
from EteintCamera import EteintCamera
import picamera

#Initialisation de la caméra et création du fichier de donées 

camera = picamera.Picamera()
f = open('donnees.txt','w')
f.write('TempÃ©rature;Altitude;Longitude;Pression,HumiditÃ©...')
f.close()

AllumeCamera()

while():
	retourALaLigne()
	sleep(20)
	ajouter(TempÃ©rature)
	ajouter(Altitude)
	ajouter(Pression)
	...
	
EteindreCamera()
MP4Box -add my_video.h264 video.mp4
