from Connexion import Connexion
from Actifs import Actifs
from Connexion import Connexion
import numpy

class VaRCov():
    def __init__(self, matrice):
        self.matrice=matrice

    def CalculMatrice(self,Connexion,date1,date2):
        
        requete1="Select distinct name from cac;"
        curseur=Connexion.execute(requete1)
        ListeNoms=[]
        #on récupère la liste des noms des actifs
        for row in curseur:
            ListeNoms.append(row['name'])
        
        Liste=[]

        for name in ListeNoms:
            ListeRendements=[]
            requete2 = "select Rendements from cac where name='"+name+"' and date between '"+date1+"' and '"+date2+"';"
            #on récupère la liste des Rendements de chaque actif
            curseur2 = Connexion.execute(requete2)    
            for row in curseur2:
                ListeRendements.append(row['Rendements'])
            if len(ListeRendements) != 7:
                Liste.append(numpy.array(ListeRendements[0:7]))
            else : Liste.append(numpy.array(ListeRendements))
 
        #print(type(Liste))
        #print(Liste)  

        Liste = numpy.array(Liste)

        matrix = numpy.cov(Liste,bias=True)

        self.matrice=matrix
        return self

# if __name__=="__main__":
#     mat = VaRCov([]) 
#     connection = Connexion('pi2','root','Leo20-Esilv')
#     connection.initialisation()
#     mat.CalculMatrice(connection,"2017-11-09","2017-11-17")
#     connection.close_connection()