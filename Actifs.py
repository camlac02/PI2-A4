# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:00:12 2022

@author: PC
"""

from sklearn.exceptions import NonBLASDotWarning
from Connexion import Connexion
import pandas
from math import nan
from django.http import request
import numpy as np

#Classe d'actifs

class Actifs():

    def __init__(self, nom, valeur, volume, date,nb_shares,rendement,poids,ListeRendementsValeurs):
        self.nom = nom
        self.valeur = valeur
        self.volume = volume
        self.date = date
        self.nb_shares = nb_shares
        self.rendement = rendement
        self.poids=poids 
        self.ListeRendementsValeurs=ListeRendementsValeurs
        #self.volatilité = 0

    def creationActifs(connexion):
        #Fonction qui prend en argument la connexion avec la base de données
        #La fonction retourne une liste d'actifs avec le nom de chaque actif 
        #Tout les autres attributs sont initialisée à 0     
        requete = 'Select distinct noms from CAC40'
        curseur = connexion.execute(requete)
        liste_Actifs = []

        for row in curseur:
            action = Actifs(row['noms'],0,0,0,0,0,0,0)
            liste_Actifs.append(action)
            
        return liste_Actifs


    def Valeur_Actifs(self, date1, date2, connection):
        #Fonction  qui prend en arguments une liste d'actifs, la date du jour
        #et la connexion avec la base de données
        #La fonction retourne une liste d'actifs, chacun asocié à une liste contenant
        #toutes les informations le concernant ('name', 'value' et 'volumnes') à la date du jour 
        requete = "Select valeurs,volumes,rendements from CAC40 where dates = '"+date1+"' and noms = '"+str(self.nom)+"';"
        curseur = connection.execute(requete)
        row = curseur.fetchone()
        self.valeur = row['valeurs']
        self.volume = row['volumes']
        self.date = date1
        self.rendement=row['rendements']
        self.poids=0
        self.RendementsPourPF(date1,date2,connection)
        return self
    
    
    def __repr__(self):
        #return "Nom : {0}, nbr d'action : {1}, r : {2};\n".format(self.nom,self.nb_shares,self.rendement)
        return "Nom : {0}, Valeur : {1}, Nbr d'Actions : {2}, \nDate : {3}\nPoids : {4}".format(self.nom,self.valeur, self.nb_shares, self.date,self.poids)

        
    def RendementsPourPF(self,date1,date2,connection):
        '''
        requete1="Select distinct noms from CAC40;"
        curseur=connection.execute(requete1)
        ListeNoms=[]
        #on récupère la liste des noms des actifs
        for row in curseur:
            ListeNoms.append(row['name'])
        Nbname=1
        for name in ListeNoms:'''
        Liste=[]
        requete2="select rendements,valeurs from CAC40 where noms='"+str(self.nom)+"' and dates between '"+date1+"' and '"+date2+"';"
        #on récupère la liste des Rendements de chaque actif
        curseur2=connection.execute(requete2)    
        for row in curseur2:
            Liste.append([row['rendements'],row['valeurs']])
        self.ListeRendementsValeurs=Liste
        print(Liste)
            #Liste.append(moyenne)
        #print(Liste)

    def Rendement_Actif(self,connexion):

        # Retourne une liste de tuple (date,rendement en %) d'un actif
        requete1 = "Select valeurs, dates from CAC40 where noms = '"+self.nom+"';"
        curseur = connexion.execute(requete1)
        valeurs_precedente = 0 
  
        for row in curseur:
            if valeurs_precedente == 0:
                self.rendement = 0
            else :
                self.rendement = (round((row['valeurs'] - valeurs_precedente)/ valeurs_precedente *100,2))
            
            valeurs_precedente = row['valeurs']

        return self
    
    def CAGR(self, date1, date2, connexion):
        requete1 = "Select valeurs from CAC40 where noms = '"+self.nom+"';"
        requete2 = "Select valeurs from CAC40 where noms = '" + self.nom + "' and dates = '"+ date1 +"';"  # Récupération de P_initial
        requete3 = "Select valeurs from CAC40 where noms ='" + self.nom + "' and dates = '"+ date2 +"';" # Récupération de P_final
        requete4 = "Select count(valeurs) from CAC40 where noms = '" + self.nom + "' and dates between '" + date1 + "' and '" +date2 + "';"
        P_init = connexion.execute(requete2)
        P_final = connexion.execute(requete3)
        nb_jours = connexion.execute(requete4)
        cagr = ((P_final / P_init) **(1/nb_jours))
        return cagr
    
    #.copy()

    ##################################  FONCTION PAS UTILISEE ################################################

    def copy(self):
        nom = self.nom
        valeur = self.valeur
        volume = self.volume
        date = self.date
        nb_shares = self.nb_shares.copy()
        rendement = self.rendement
        Actif = Actifs(nom,valeur,volume,date,nb_shares,rendement)
        return Actif
    
    def MoyenneRendements(self,date1,date2,connection):
        Liste=[]
        requete1="Select distinct noms from CAC40;"
        curseur=connection.execute(requete1)
        ListeNoms=[]
        #on récupère la liste des noms des actifs
        for row in curseur:
            ListeNoms.append(row['noms'])
        for name in ListeNoms:
            somme=0
            requete2="select rendements from CAC40 where noms='"+name+"' and dates between '"+date1+"' and '"+date2+"';"
            #on récupère la liste des Rendements de chaque actif
            curseur2=connection.execute(requete2)    
            nbrow=0
        for row in curseur2:
            somme+=(row['rendements'])
            nbrow+=1
        moyenne=round(somme,6)
        if(self.nom==name):
            self.moyenneRendements=moyenne
        #Liste.append(moyenne)
    #print(Liste)

    #############################################################################################################
