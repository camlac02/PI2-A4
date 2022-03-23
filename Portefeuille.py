# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:13:52 2022

@author: PC
"""
from Actifs import Actifs
import random
from VaRCov import VaRCov
from Connexion import Connexion
from Fitness import fitness
import math
import numpy as np
#pour copier la liste d'actif et pas faire de doublons
from copy import deepcopy

class Portefeuille():

    def __init__(self, liste_Actifs, valeur, volatilite, rendement, score):
        self.liste_Actifs = liste_Actifs
        self.valeur = valeur
        self.volatilite = volatilite
        self.rendement = rendement
        self.score = score


    # Calcul le prix de l'actif avec le plus faible 
    def plus_petit_prix(liste_Actif):
        min = liste_Actif[0].valeur
        for asset in liste_Actif:
            if asset.valeur < min:
                min = asset.valeur
        return min 

    #Créé un portefeuil composé d'une liste d'action aléatoire
    def Creation_Portefeuille(self, MaxInvesti):

        #pour copier la liste d'actif et pas faire de doublons
        liste_Actif = deepcopy(self.liste_Actifs)

        prix_min = Portefeuille.plus_petit_prix(liste_Actif) 
        action = list(range(len(liste_Actif))) # liste des index de tous les actifs du portefeuille   

        #On reinitialise la valeur des nb_shares
        for i in range(len(liste_Actif)):
            liste_Actif[i].nb_shares = 0

        while (MaxInvesti > prix_min and len(action) !=0 ):
        # Tant que la valeur a investir (MaxInvest) est superieur au prix de l'actif le moins cher
        # Et tant que la liste des index des actifs du portefeuil n'est pas vide
        # on ajoute une action au portefeuill

            # Selection aléatoire d'une action via son index dans la liste d'actif
            choix_action = random.choice(action)
            action.remove(choix_action) # On retire l'index de la liste pour ne pas tomber deux fois sur le même actif

            # Nombre maximal de shares que l'on peut acheter pour cet actif
            max_nb = MaxInvesti//(liste_Actif[choix_action].valeur)
            # Selection du nombre de shares entre 0 et nb_max 

            #self.liste_nbr_shares[choice_asset] = random.randint(0,max_nb)
            rnd = random.randint(0,max_nb)
            liste_Actif[choix_action].nb_shares = rnd
            # On reduit la valeur a investir en lui retirant la valeur des parts de l'actif choisi
            MaxInvesti = MaxInvesti - liste_Actif[choix_action].nb_shares*liste_Actif[choix_action].valeur
            #MaxInvesti = MaxInvesti - int(self.liste_nbr_shares[choice_asset])*self.liste_Actifs[choice_asset].valeur

        self.liste_Actifs = liste_Actif
        self.Valeur_Portefeuille()
        self.Poid_dans_portefeuille() # calcule la valeur finale du portefeuille
        self.VolPortefeuille(liste_Actif)
        self.RendementsPF(liste_Actif)

        self.score = fitness(self, 0).RatioSharpe()

        return self


    # Calcul la valeur d'un portefeuille
    def Valeur_Portefeuille(self):
        #Fonction qui prend en argument un portefeuille et qui calcule
        #la valeur associée à ce portefeuille 
        self.valeur = 0
        for i in range(len( self.liste_Actifs)):
            #valeur=valeur asset*poids
            self.valeur = self.valeur +  self.liste_Actifs[i].valeur*int( self.liste_Actifs[i].nb_shares)
            #self.valeur = self.valeur +  self.liste_Actifs[i].valeur*int( self.liste_nbr_shares [i])
        return self


    def VolPortefeuille(self,listeActif):
        self.volatilite = 0
        Listepoids=[]
        for actif in self.liste_Actifs:
            Listepoids.append(actif.poids)
        Listepoids=np.array(Listepoids)
        #print(Listepoids)
        mat = VaRCov([]) 
        connection = Connexion('pi2','root','Leo20-Esilv')
        connection.initialisation()
        mat.CalculMatrice(connection,"2017-01-05","2017-12-29")
        matrice = mat.matrice
        #print('matrice : \n',matrice)
        connection.close_connection()
        vol = math.sqrt((np.transpose(Listepoids)@matrice@Listepoids))
        print("vol",vol)
        self.volatilite=vol
        return self
    
    # def RendementsPF(self,liste_Actif):
    #     self.rendement = 0
    #     liste = []
    #     for i in range(0,len(liste_Actif[1].ListeRendementsValeurs)-1):
    #         liste.append(np.prod([x+1 for x in liste_Actif[i].ListeRendementsValeurs])**(1/len(liste_Actif[i].ListeRendementsValeurs))-1)
    #     self.rendement = (sum([a*b for a,b in zip([liste_Actif[i].nb_shares for i in range(0,len(liste_Actif[1].ListeRendementsValeurs))], liste)]))/100
    #     return self

    def RendementsPF(self, liste_Actif):
        liste_Actif = self.liste_Actifs
        RendementPF =0
        Liste=[]
        SommePF=1
        for j in range(0,len(liste_Actif[1].ListeRendementsValeurs) -1):
            RendementPF =0
            for i in liste_Actif:
                Liste=i.ListeRendementsValeurs
                RendementPF+=Liste[j][0]*i.nb_shares*Liste[j][1]/self.valeur
            SommePF*=(1+RendementPF)
        self.rendement = SommePF-1


    def __repr__(self):
        return "\nValeur du Portefeuille : {0}\nVolatilité :{1}\nrendement :{2}\nScore du portefeuille (Ratio Sharpe) :  {3}\n".format(self.valeur,self.volatilite,self.rendement,self.score) 
    
    def __str__(self):
        return "\nListe d'actifs : {0}\n".format(self.liste_Actifs) 

    def mutation(self,MaxInvest):

        liste_Actif = deepcopy(self.liste_Actifs)
        # self.score = 0
        # self.rendement = 0
        # self.volatilite = 0
        valeur_totale = deepcopy(self.valeur)

        r = random.randrange(0,len(liste_Actif))
        while (liste_Actif[r].nb_shares == 0):
            r = random.randrange(0,len(liste_Actif))

        # retire la valeur de l'actif au portefeuille
        MaxInvest = liste_Actif[r].valeur * liste_Actif[r].nb_shares + (MaxInvest - valeur_totale) #on obtient la valeur de l'actif retiré ainsi que l'espace restant du portefeuil
        print('MaxInvest  : '+str(MaxInvest) )
        liste_Actif[r].nb_shares = 0
        #valeur_totale = valeur_totale - liste_Actif[r].valeur * liste_Actif[r].nb_shares
        print("Nom de l'action Mutée : "+ liste_Actif[r].nom)

        prix_min = Portefeuille.plus_petit_prix(liste_Actif) 
        action = list(range(len(liste_Actif))) # liste des index de tous les actifs du portefeuille   

        action.remove(r) #On retire l'actif qu'on vient de retirer du portefeuille de la liste

        #On realise la même manipulation que pour creation_portefeuille
        while (MaxInvest > prix_min and len(action) !=0):

            choix_action = random.choice(action)
            action.remove(choix_action) 

            max_nb = MaxInvest//(liste_Actif[choix_action].valeur)

            rnd = random.randint(0,max_nb)
            liste_Actif[choix_action].nb_shares = rnd + liste_Actif[choix_action].nb_shares         
            
            valeur = rnd*liste_Actif[choix_action].valeur
            MaxInvest = MaxInvest - valeur

        self.liste_Actifs = liste_Actif

        self.Valeur_Portefeuille()

        self.Poid_dans_portefeuille() # calcule la valeur finale du portefeuille
        self.VolPortefeuille(liste_Actif)
        self.RendementsPF(liste_Actif)

        self.score = fitness(self, 0).RatioSharpe()
        
        print('PORTEFEUILLE MUTE')
        print(self.__repr__())

        return self

    #################################################################################################################################
    #Defini le poid qu'a l'action dans le portefeuille
    def Poid_dans_portefeuille(self):

        for i in range(len(self.liste_Actifs)):
            self.liste_Actifs[i].poids = 0
            poids = self.liste_Actifs[i].valeur * self.liste_Actifs[i].nb_shares
            self.liste_Actifs[i].poids  = round(poids / self.valeur,5)
        return self
    ####################################################################################################################################
  
