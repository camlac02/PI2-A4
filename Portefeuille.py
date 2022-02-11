#Classe Portefeuille
from Actifs import Actifs
import random

#pour copier la liste d'actif et pas faire de doublons
from copy import deepcopy

class Portefeuille():

    def __init__(self, liste_Actifs, valeur, score):
        self.liste_Actifs = liste_Actifs
        self.valeur = valeur
        self.score = score


    # Calcul le prix de l'actif avec le plus faible 
    def plus_petit_prix(liste_Actif):
        min = liste_Actif[0].valeur
        for asset in liste_Actif:
            if asset.valeur < min:
                min = asset.valeur
        return min 

    def score_portefeuille(self):
        self.score = round(random.random(),4)
        return self

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
        self.score_portefeuille() #AJOUTE SCORE AU PORTEFEUILLE
        #self.Poid_dans_portefeuille()
        return self


    # Calcul la valeur d'un portefeuille
    def Valeur_Portefeuille(self):
        #Fonction qui prend en argument un portefeuille et qui calcule
        #la valeur associée à ce portefeuille 
        self.liste_Actifs
        for i in range(len( self.liste_Actifs)):
            #valeur=valeur asset*poids
            self.valeur = self.valeur +  self.liste_Actifs[i].valeur*int( self.liste_Actifs[i].nb_shares)
            #self.valeur = self.valeur +  self.liste_Actifs[i].valeur*int( self.liste_nbr_shares [i])
        return self


    def __repr__(self):
        #return "{0}\nValeur du portefeuil : {2}\nScore du portefeuille : {1}\n\n".format(self.liste_Actifs,self.score,self.valeur) 
        return "Valeur du Portefeuille : {0}\nScore du portefeuille :  {1}\n".format(self.valeur,self.score) 


    def mutation(self,MaxInvest):

        r = random.randrange(0,len(self.liste_Actifs))
        while (self.liste_Actifs[r].nb_shares == 0):
            r = random.randrange(0,len(self.liste_Actifs))

        # retire la valeur de l'actif au portefeuille
        self.valeur -= MaxInvest
        self.liste_Actifs[r].nb_shares = 0
        print("Nom de l'action Mutée : "+self.liste_Actifs[r].nom)

        prix_min = Portefeuille.plus_petit_prix(self.liste_Actifs) 
        action = list(range(len(self.liste_Actifs))) # liste des index de tous les actifs du portefeuille   

        action.remove(r) #On retire l'actif qu'on vient de retirer du portefeuille de la liste

        #On realise la même manipulation que pour creation_portefeuille
        while (MaxInvest > prix_min and len(action) !=0 ):

            choix_action = random.choice(action)
            action.remove(choix_action) 

            max_nb = MaxInvest//(self.liste_Actifs[choix_action].valeur)

            rnd = random.randint(0,max_nb)
            self.liste_Actifs[choix_action].nb_shares = rnd
            
            valeur = self.liste_Actifs[choix_action].nb_shares*self.liste_Actifs[choix_action].valeur
            MaxInvest = MaxInvest - valeur

            self.valeur += valeur #On ajoute la valeur des actions a la valeur du portefeuille

        return self

    #################################################################################################################################
    #Defini le poid qu'a l'action dans le portefeuille
    def Poid_dans_portefeuille(self):
        for i in range(len(self.liste_Actifs)):
            poids = self.liste_Actifs[i].valeur * self.liste_Actifs[i].nb_shares
            self.liste_Actifs[i].poids  = round(poids / self.Valeur_Portefeuille()*100,2)
        return self
    ####################################################################################################################################
    
    