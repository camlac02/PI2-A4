from Connexion import Connexion
from Actifs import Actifs
import numpy as np

class VaRCov():
    #Attributs
    def __init__(self, matrice):
        self.matrice=matrice

    #Calcul de la matrice variance covariance
    def CalculMatrice(self,Connexion,date1,date2):
        Liste=[]
        #Récupération des Noms des actifs pour les parcourir et récupérer les rendements
        requete1="Select distinct Noms from cac;"
        curseur=Connexion.execute(requete1)
        ListeNoms=[]
        #On récupère la liste des noms des actifs
        for row in curseur:
            ListeNoms.append(row['Noms'])
        
        for name in ListeNoms:
            ListeRendements=[]
            #Récupération des Rendements des actifs entre 2 dates
            requete2="select Rendements from cac where Noms ='"+name+"' and Dates between '"+date1+"' and '"+date2+"';"
            #On récupère la liste des Rendements de chaque actif
            curseur2=Connexion.execute(requete2)    
            for row in curseur2:
                #Pour tous les actifs, pour toutes les dates, on ajoute les rendements dans la matrice
                ListeRendements.append(row['Rendements'])
            Liste.append(ListeRendements)
        #Création de la matrice variance covariance
        matrix=np.cov(Liste,bias=True)
        self.matrice=matrix



if __name__=="__main__":
    mat = VaRCov([]) 
    connection = Connexion('pi2','root','root')
    connection.initialisation()
    mat.CalculMatrice(connection,"2017-11-09","2017-11-17")
    connection.close_connection()