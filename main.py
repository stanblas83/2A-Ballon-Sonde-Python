from time import sleep

f = open('donnees.txt','w')
f.write('TempÃ©rature;Altitude;Longitude;Pression,HumiditÃ©...')
f.close()
AllumeCamera()

while():
	retourALaLigne()
	sleep(10)
	ajouter(TempÃ©rature)
	ajouter(Altitude)
	ajouter(Pression)
	...
	
EteindreCamera()
