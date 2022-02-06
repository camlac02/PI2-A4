from Connexion import Connexion
from Actifs import Actifs
from Connexion import Connexion
import numpy as np

class VaRCov():
    def __init__(self, matrice):
        self.matrice=matrice

    def CalculMatrice(self,Connexion,date1,date2):
        Liste=[]
        requete1="Select distinct name from helo;"
        curseur=Connexion.execute(requete1)
        ListeNoms=[]
        #on récupère la liste des noms des actifs
        for row in curseur:
            ListeNoms.append(row['name'])
        
        for name in ListeNoms:
            ListeRendements=[]
            requete2="select Rendements from helo where name='"+name+"' and date between '"+date1+"' and '"+date2+"';"
            #on récupère la liste des Rendements de chaque actif
            curseur2=Connexion.execute(requete2)    
            for row in curseur2:
                ListeRendements.append(row['Rendements'])
            Liste.append(ListeRendements)
        #print(type(Liste))
        #print(Liste)
        matrix=np.cov(Liste,bias=True)
        #print(matrix)
        self.matrice=matrix



if __name__=="__main__":
    mat = VaRCov([]) 
    connection = Connexion('cac','root','Jhanamal0004@')
    connection.initialisation()
    mat.CalculMatrice(connection,"2017-11-09","2017-11-17")
    connection.close_connection()

