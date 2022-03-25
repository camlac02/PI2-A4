import random
from VaRCov import VaRCov
from Fitness import fitness
import math
import numpy as np

#pour copier la liste d'actif et pas faire de doublons
from copy import deepcopy

#Classe Portefeuille
class Portefeuille():

    def __init__(self, liste_Actifs, valeur, volatilite, rendement, score):
        self.liste_Actifs = liste_Actifs
        self.valeur = valeur
        self.volatilite = volatilite
        self.rendement = rendement
        self.score = score



    # Calcul du prix de l'actif avec le moins de valeur
    def plus_petit_prix(liste_Actif):
        min = liste_Actif[0].valeur
        for asset in liste_Actif:
            if asset.valeur < min:
                min = asset.valeur
        #retourne le prix le plus faible
        return min 



    #Créé un portefeuil composé d'une liste d'action aléatoire
    def Creation_Portefeuille(self, MaxInvesti,date_1,date_2,connexion):

        #pour copier la liste d'actif et pas faire de doublons
        liste_Actif = deepcopy(self.liste_Actifs)
        prix_min = Portefeuille.plus_petit_prix(liste_Actif) 
        action = list(range(len(liste_Actif))) #liste des index de tous les actifs du portefeuille   

        #On reinitialise la valeur des nb_shares par précaution
        for i in range(len(liste_Actif)):
            liste_Actif[i].nb_shares = 0

        while (MaxInvesti > prix_min and len(action) !=0 ):
        # Tant que la valeur a investir (MaxInvest) est superieur au prix de l'actif le moins cher
        # Et tant que la liste des index des actifs du portefeuil n'est pas vide
        # on ajoute une action au portefeuille

            # Selection aléatoire d'une action via son index dans la liste d'actif
            choix_action = random.choice(action)
            action.remove(choix_action) # On retire l'index de la liste pour ne pas tomber deux fois sur le même actif

            # Nombre maximal de shares que l'on peut acheter pour cet actif
            max_nb = MaxInvesti//(liste_Actif[choix_action].valeur)
            # Selection du nombre de shares entre 0 et nb_max 
            rnd = random.randint(0,max_nb)
            liste_Actif[choix_action].nb_shares = rnd

            # On reduit la valeur a investir en lui retirant la valeur des parts de l'actif choisi
            MaxInvesti = MaxInvesti - liste_Actif[choix_action].nb_shares*liste_Actif[choix_action].valeur

        self.liste_Actifs = liste_Actif
        #On associe une valeur, une volatilité ainsi qu'un rendement au portefeuille
        #Et on associe un poid a chaque actif dans le portefeuille
        self.Valeur_Portefeuille()
        self.Poid_dans_portefeuille()
        self.VolPortefeuille(date_1,date_2,connexion)
        self.RendementsPF()
        #On calcul le score du portefeuille grace a la fitness
        self.score = fitness(self, 0).RatioSharpe()

        return self



    #Calcul la valeur d'un portefeuille
    def Valeur_Portefeuille(self):
        #Fonction qui prend en argument un portefeuille et qui calcule
        #la valeur associée à ce portefeuille 
        self.valeur = 0
        for i in range(len( self.liste_Actifs)):
            #valeur = valeur_asset * nb_shares
            self.valeur = self.valeur +  self.liste_Actifs[i].valeur*int( self.liste_Actifs[i].nb_shares)
        return self



    
    def Poid_dans_portefeuille(self):
        #Defini le poid qu'on les actions dans le portefeuille
        for i in range(len(self.liste_Actifs)):
            self.liste_Actifs[i].poids = 0
            poids = self.liste_Actifs[i].valeur * self.liste_Actifs[i].nb_shares
            self.liste_Actifs[i].poids  = round(poids / self.valeur,5)
        return self



    #Calcule la volatilité d'un portefeuille entre deux dates
    def VolPortefeuille(self,date_1,date_2,connexion):
        self.volatilite = 0
        Listepoids=[]
        for actif in self.liste_Actifs:
            Listepoids.append(actif.poids)

        Listepoids=np.array(Listepoids)
        mat = VaRCov([]) 
        mat.CalculMatrice(connexion,date_1,date_2)
        matrice = mat.matrice
        vol = math.sqrt((np.transpose(Listepoids)@matrice@Listepoids))

        self.volatilite=vol



    #Calcule le rendement d'un portefeuille (Rendements PorteFeuille)
    def RendementsPF(self):
        liste_Actif = self.liste_Actifs
        RendementPF = 0
        Liste = []
        SommePF = 1
        for j in range(0,len(liste_Actif[1].ListeRendementsValeurs) -1):
            RendementPF =0
            for i in liste_Actif:
                Liste=i.ListeRendementsValeurs
                RendementPF+=Liste[j][0]*i.nb_shares*Liste[j][1]/self.valeur
            SommePF*=(1+RendementPF)

        self.rendement = SommePF-1



    #Fonction permettant de muter un portefeuille d'une population
    #Fonctionne comme la fonction 'Creation_Portefeuille' en retirant la valeur d'un actif
    #Et en le remplacant par d'autres actifs séléctionnés aléatoirement
    def mutation(self,MaxInvest,date_1,date_2,connexion):

        liste_Actif = deepcopy(self.liste_Actifs) #On utilise deepcopy pour éviter les doublons
        valeur_totale = deepcopy(self.valeur)

        r = random.randrange(0,len(liste_Actif))
        while (liste_Actif[r].nb_shares == 0):
            r = random.randrange(0,len(liste_Actif))

        #On retire la valeur de l'actif au portefeuille
        MaxInvest = liste_Actif[r].valeur * liste_Actif[r].nb_shares + (MaxInvest - valeur_totale) #on obtient la valeur de l'actif retiré ainsi que l'espace restant du portefeuil
        print('Valeur libérée : '+str(MaxInvest))
        liste_Actif[r].nb_shares = 0
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
        self.Poid_dans_portefeuille()
        self.VolPortefeuille(date_1,date_2,connexion)
        self.RendementsPF()
        self.score = fitness(self, 0).RatioSharpe()
        
        print('\nPORTEFEUILLE MUTE : ')
        print(self.__repr__())

        return self



    #Retourne une chaine de caractere décrivant un portefeuille
    def __repr__(self):
        return "\nValeur du Portefeuille : {0}\nVolatilité :{1}\nrendement :{2}\nScore du portefeuille (Ratio Sharpe) :  {3}\n".format(self.valeur,self.volatilite,self.rendement,self.score) 
    


    #Retourne une chaine de caractere composé de la liste des actions contenu dans un portefeuille
    #Et les informations associées à ces actions
    def __str__(self):
        return "\nListe d'actifs : {0}\n".format(self.liste_Actifs) 
