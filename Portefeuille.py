#Classe Portefeuille
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

    def __init__(self, liste_Actifs, valeur, score):
        self.liste_Actifs = liste_Actifs
        self.valeur = valeur
        self.score = score

    '''
    #Cree une liste d'actif avec leur prix a une date choisit
    def Creation_list_actif(connection, date):
           
        list_asset_with_value = []
        list_asset = Actifs.creationActifs(connection)
        #Associe une valeur a chaque actif
        for asset in list_asset:
                list_asset_with_value.append(asset.Valeur_Actifs(date,connection)) 
        return list_asset_with_value
    '''

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
        liste_Actif = copy.deepcopy(self.liste_Actifs)

        prix_min = Portefeuille.plus_petit_prix(liste_Actif) 
        action = list(range(len(liste_Actif))) # liste des index de tous les actifs du portefeuille   

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

        self.Valeur_Portefeuille(liste_Actif) #calule les poids
       
        self.Poid_dans_portefeuille(liste_Actif) # calcule la valeur finale du portefeuille
        #self.VolPortefeuille(liste_Actif)
        self.liste_Actifs = liste_Actif
        
        return self


    # Calcul la valeur d'un portefeuille
    def Valeur_Portefeuille(self,liste_Actifs):
        #Fonction qui prend en argument un portefeuille et qui calcule
        #la valeur associée à ce portefeuille 
        for i in range(len( liste_Actifs)):
            #valeur=valeur asset*poids
            self.valeur = self.valeur + liste_Actifs[i].valeur*int( liste_Actifs[i].nb_shares)
            #self.valeur = self.valeur +  self.liste_Actifs[i].valeur*int( self.liste_nbr_shares [i])


    #################################################################################################################################
    #Defini le poids qu'a l'action dans le portefeuille
    def Poid_dans_portefeuille(self,liste_Actif):
        for i in range(len(liste_Actif)):
            poids = liste_Actif[i].valeur * liste_Actif[i].nb_shares
            liste_Actif[i].poids  = round(poids / self.valeur*100,2)
    ####################################################################################################################################
    
    def VolPortefeuille(self,listeActif):
        Listepoids=[]
        for i in listeActif:
            Listepoids.append(i.poids)
        mat = VaRCov([]) 
        connection = Connexion('cac','root','Jhanamal0004@')
        connection.initialisation()
        matrice=mat.CalculMatrice(connection,"2017-11-09","2017-11-17")
        connection.close_connection()
        vol=math.sqrt(np.transpose(Listepoids)@(matrice@Listepoids))
        self.score=vol
        
    def __repr__(self):
        return "{0}\nValeur du portefeuil : {2}\nScore du portefeuille : {1}\n\n".format(self.liste_Actifs,self.score,self.valeur) 
           
