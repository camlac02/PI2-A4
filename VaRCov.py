from Connexion import Connexion
from Actifs import Actifs
from Connexion import Connexion
import numpy as np

class VaRCov():
    def __init__(self, matrice):
        self.matrice=matrice

def CalculMatrice(Connexion,date1,date2):
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
    Liste2=np.array(Liste)
    print(Liste2[1])
    #np.cov()
    #matrix=np.cov(Liste2,bias=True)
    #print(matrix)

    '''A = [45.2,37,42,35,39]
    B = [38,31,26,28,33]
    C = [10,15,17,21,12]
    Liste1=[]
    Liste1.append(A)
    Liste1.append(B)
    Liste1.append(C)
    data=np.array(Liste1)
    covMatrix = np.cov(data,bias=True)
    print (covMatrix)
    ''' 
    return 0

if __name__=="__main__":
    connection = Connexion('cac','root','Jhanamal0004@')
    connection.initialisation()
    CalculMatrice(connection,"03/11/2021","05/11/2021")
    connection.close_connection()
    
        