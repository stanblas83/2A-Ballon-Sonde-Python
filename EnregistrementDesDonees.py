def CreationDuFichierCsv(Entete):
  f=('DonéesDeVol.csv','w')
  ligneEntete=";".join(Entete)+"\n"
  f.write(ligneEntete)
  f.close()
  
  
def ajouterUneLigne(Ligne):
  f=('DonéesDeVol.csv','a')
  ligne=";".join(Ligne)+"\n"
  f.write(ligneEntete)
  f.close()
