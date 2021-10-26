from AllumeCamera import AllumeCamera
from Capteurs import Capteurs
from EteintCamera import EteintCamera
from EteintRaspberry import EteintRaspberry
from time import sleep

def GestionVol () :
  a1=0
  a2=-1000
  AllumeCamera()
  a1=Capteurs()
  sleep(60)
  while (a1>5000 | a1>=a2)
    a2=a1
    a1=Capteurs()
    sleep(10)
  EteintCamera()
  while (a1<a2)
    a2=a1
    a1=Capteurs()
    sleep(10)
  EteintRaspberry();
  return
