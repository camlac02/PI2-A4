import numpy as np

class VaRCov():
    def __init__(self, matrice):
        self.matrice=matrice
        
    #Calcul de la matrice de variance covariance
    def CalculMatrice(self,Connexion,date1,date2):
        Liste=[]
        requete1="Select distinct name from cac;"
        curseur=Connexion.execute(requete1)
        ListeNoms=[]
        #on récupère la liste des noms des actifs
        for row in curseur:
            ListeNoms.append(row['name'])
        
        for noms in ListeNoms:
            ListeRendements=[]
            requete2="select Rendements from cac where name='"+noms+"' and date between '"+date1+"' and '"+date2+"';"
            #on récupère la liste des Rendements de chaque actif
            curseur2 = Connexion.execute(requete2)    
            for row in curseur2:
                ListeRendements.append(row['Rendements'])
            if len(ListeRendements) != 7:
                Liste.append(np.array(ListeRendements[0:7]))
            else : Liste.append(np.array(ListeRendements))
 
        Liste = np.array(Liste)
        matrix=np.cov(Liste,bias=True)
        self.matrice=matrix

