from re import M
from Actifs import Actifs
from VaRCov import VaRCov
from Connexion import Connexion
import  random

#pour copier la liste d'actif et pas faire de doublons
import copy
import math
import numpy as np
class Portefeuille():

    #Attributs
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

    #Créé un portefeuille composé d'une liste d'action aléatoire
    def Creation_Portefeuille(self, MaxInvesti):

        #Pour copier la liste d'actif et pas faire de doublons
        liste_Actif = copy.deepcopy(self.liste_Actifs)

        #Définition de l'actif ayant le plus petit prix
        prix_min = Portefeuille.plus_petit_prix(liste_Actif) 
        action = list(range(len(liste_Actif))) #Liste des index de tous les actifs du portefeuille   

        for i in range(len(liste_Actif)):
            liste_Actif[i].nb_shares = 0

        while (MaxInvesti > prix_min and len(action) !=0 ):
        #Tant que la valeur a investir (MaxInvest) est superieur au prix de l'actif le moins cher
        #Et tant que la liste des index des actifs du portefeuil n'est pas vide
        #On ajoute une action au portefeuille

            #Selection aléatoire d'une action via son index dans la liste d'actif
            choix_action = random.choice(action)
            action.remove(choix_action) # On retire l'index de la liste pour ne pas tomber deux fois sur le même actif

            #Nombre maximal de shares que l'on peut acheter pour cet actif
            max_nb = MaxInvesti//(liste_Actif[choix_action].valeur)
            #Selection du nombre de shares entre 0 et nb_max 

            rnd = random.randint(0,max_nb)
            liste_Actif[choix_action].nb_shares = rnd
            #On reduit la valeur a investir en lui retirant la valeur des parts de l'actif choisi
            MaxInvesti = MaxInvesti - liste_Actif[choix_action].nb_shares*liste_Actif[choix_action].valeur
            #MaxInvesti = MaxInvesti - int(self.liste_nbr_shares[choice_asset])*self.liste_Actifs[choice_asset].valeur

        #Définition des attributs à l'aide des éléments des actifs et les fonctions
        self.Valeur_Portefeuille(liste_Actif) #calule les poids
        self.Poid_dans_portefeuille(liste_Actif) # calcule la valeur finale du portefeuille
        self.VolPortefeuille(liste_Actif)
        self.RendementsPF(liste_Actif)
        self.RatioSharpe()
        self.liste_Actifs = liste_Actif
        
        return self


    #Calcul la valeur d'un portefeuille
    def Valeur_Portefeuille(self,liste_Actifs):
        #Fonction qui prend en argument un portefeuille et qui calcule
        #la valeur associée à ce portefeuille 
        for i in range(len( liste_Actifs)):
            self.valeur = self.valeur + liste_Actifs[i].valeur*int( liste_Actifs[i].nb_shares)

    #################################################################################################################################
    #Definition du poids de l'action dans le portefeuille
    def Poid_dans_portefeuille(self,liste_Actif):
        for i in range(len(liste_Actif)):
            poids = liste_Actif[i].valeur * liste_Actif[i].nb_shares
            liste_Actif[i].poids  = round(poids / self.valeur,5)
    ####################################################################################################################################
    
    #Calcul de la volatilité du portefeuille
    def VolPortefeuille(self,listeActif):
        Listepoids=[]
        #Association des poids aux actifs pour calculer la volatilité à l'aide de la matrice variance covariance
        for i in listeActif:
            Listepoids.append(i.poids)
        Listepoids=np.array(Listepoids)
        mat = VaRCov([]) 
        #Requête et récupération de la matrice variance covariance
        connection = Connexion('pi2','root','root')
        connection.initialisation()
        mat.CalculMatrice(connection,"2018-11-01","2018-11-30")
        matrice=mat.matrice
        connection.close_connection()
        #Calcul de la volatilité à l'aide d'un produit matriciel
        vol=math.sqrt((np.transpose(Listepoids))@matrice@Listepoids)
        print("Volatilité :",vol)
        self.volatilite=vol
    
    #Calcul du rendement du portefeuille
    def RendementsPF(self, liste_Actif):
        RendementPF =0
        Liste=[]
        Rend=1
        #On parcourt la liste des rendements et valeur créé pour chaque actif
        for j in range(len(liste_Actif[1].ListeRendementsValeurs)):
            RendementPF =0
            for i in liste_Actif:
                Liste=i.ListeRendementsValeurs
                #Pour calculer le rendement du portefeuille on ajoute chaque valeur d'actifs multipliés par le nombre de share et le rendement de l'actif
                RendementPF+=Liste[j][0]*i.nb_shares*Liste[j][1]/self.valeur
            #On multiplie pour chaque actif le rendement du portefeuille par 1 + le rendement obtenu précédemment
            Rend*=(1+RendementPF)
        #Enfin, on retranche 1 à Rend pour obtenir la valeur du rendement final du portefeuille
        self.rendement = Rend-1
    
    #On calcule le ratio de Sharpe en faisant le rendement sur la volatilité
    def RatioSharpe(self):
        ratio = (self.rendement)/(self.volatilite)
        self.score = ratio
    
    #Fonction mutation pour générer de nouveaux portefeuilles
    def mutation(self,MaxInvest):
        
        liste_Actif = copy.deepcopy(self.liste_Actifs)
    
        r = random.randrange(0,len(liste_Actif))
        while (liste_Actif[r].nb_shares == 0):
            r = random.randrange(0,len(liste_Actif))

        MaxInvest-=liste_Actif[r].valeur*liste_Actif[r].nb_shares
        #On retire la valeur de l'actif au portefeuille
        liste_Actif[r].nb_shares = 0
        print("Nom de l'action Mutée : "+liste_Actif[r].nom)

        prix_min = Portefeuille.plus_petit_prix(liste_Actif) 
        action = list(range(len(liste_Actif))) #Liste des index de tous les actifs du portefeuille   

        action.remove(r) #On retire l'actif qu'on vient de retirer du portefeuille de la liste

        #On realise la même manipulation que pour creation_portefeuille
        while (MaxInvest > prix_min and len(action) !=0 ):

            choix_action = random.choice(action)
            action.remove(choix_action) 

            max_nb = MaxInvest//(liste_Actif[choix_action].valeur)

            rnd = random.randint(0,max_nb)
            liste_Actif[choix_action].nb_shares = rnd
            
            valeur = liste_Actif[choix_action].nb_shares*liste_Actif[choix_action].valeur
            MaxInvest = MaxInvest - valeur

        self.Valeur_Portefeuille(liste_Actif) #Calul des poids
        self.Poid_dans_portefeuille(liste_Actif) #Calcul de la valeur finale du portefeuille
        self.VolPortefeuille(liste_Actif)
        self.RendementsPF(liste_Actif)
        self.RatioSharpe()
        self.liste_Actifs = liste_Actif

        return self
        
    def __repr__(self):
        return "\nListe Actifs : {0}, \nValeur portefeuille : {1}, \nSharpe : {2}, \nVol : {3}\nRendementPF : {4}".format(self.liste_Actifs,self.valeur, self.score, self.volatilite,self.rendement)
