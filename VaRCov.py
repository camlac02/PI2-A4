# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:00:08 2022

@author: PC
"""
from Connexion import Connexion
from Actifs import Actifs
from Connexion import Connexion
import numpy as np

class VaRCov():
    def __init__(self, matrice):
        self.matrice=matrice

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
 
        #print(type(Liste))
        #print(Liste)  

        Liste = np.array(Liste)

        #print(type(Liste))
        #print(Liste)
        matrix=np.cov(Liste,bias=True)
        #print(matrix)
        self.matrice=matrix

