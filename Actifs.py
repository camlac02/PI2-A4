from Connexion import Connexion
import pandas
from math import nan
from django.http import request
import numpy as np

#Classe d'actifs

class Actifs():

    #Attributs
    def __init__(self, nom, valeur, volume, date,nb_shares,rendement,poids,ListeRendementsValeurs):
        self.nom = nom
        self.valeur = valeur
        self.volume = volume
        self.date = date
        self.nb_shares = nb_shares
        self.rendement = rendement
        self.poids=poids 
        self.ListeRendementsValeurs=ListeRendementsValeurs

    def creationActifs(connexion):
        #Fonction qui prend en argument la connexion avec la base de données
        #La fonction retourne une liste d'actifs avec le nom de chaque actif 
        #Tout les autres attributs sont initialisée à 0     
        requete = 'Select distinct Noms from cac'
        curseur = connexion.execute(requete)
        liste_Actifs = []

        #On initialise tous les éléments de l'actifs créé
        for row in curseur:
            action = Actifs(row['Noms'],0,0,0,0,0,0,0)
            liste_Actifs.append(action)
            
        return liste_Actifs


    def Valeur_Actifs(self, date1, date2, connection):
        #Sélection des valeurs, volumes, rendements que l'on associe aux attributs de l'actif
        requete = "Select Valeurs,Volumes,Rendements from cac where date = '"+date1+"' and Noms = '"+str(self.nom)+"';"
        curseur = connection.execute(requete)
        row = curseur.fetchone()

        self.valeur = row['Valeurs']
        self.volume = row['Volumes']
        self.date = date1
        self.rendement=row['Rendements']
        #Initialisation du poids à 0 pour tous les actifs
        self.poids=0
        #Utilisation de la fonction RendementsPourPF
        self.RendementsPourPF(date1,date2,connection)
        return self
    
    #Fonction qui renvoie le rendement de l'actif
    def Rendement_Actif(self,connexion):
        #Retourne une liste de tuple (date,rendement en %) d'un actif
        requete1 = "Select Valeurs, date from cac where Noms = '"+self.nom+"';"
        curseur = connexion.execute(requete1)
        valeurs_precedente = 0 
        #On parcourt les actifs et on associe aux rendements la valeur a laquelle on retranche la valeur précédente 
        for row in curseur:
            if valeurs_precedente == 0:
                self.rendement = 0
            else :
                self.rendement = (round((row['Valeurs'] - valeurs_precedente)/ valeurs_precedente *100,2))
            
            valeurs_precedente = row['Valeurs']

        return self

    #Fonction qui créé une liste de rendements et valeurs entre 2 dates 
    def RendementsPourPF(self,date1,date2,connection):
        Liste=[]
        requete2="select Rendements,Valeurs from cac where Noms ='"+str(self.nom)+"' and date between '"+date1+"' and '"+date2+"';"
        #On récupère la liste des Rendements de chaque actif
        curseur2=connection.execute(requete2)    
        for row in curseur2:
            Liste.append([row['Rendements'],row['Valeurs']])
        self.ListeRendementsValeurs=Liste
        #print(Liste)
    

    def __repr__(self):
        #return "Nom : {0}, nbr d'action : {1}, r : {2};\n".format(self.nom,self.nb_shares,self.rendement)
        return "Nom : {0}, Valeur : {1}, Nbr d'Actions : {2}, \nDate : {3}\nPoids : {4}".format(self.nom,self.valeur, self.nb_shares, self.date,self.poids)