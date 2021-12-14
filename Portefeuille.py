#Classe Portefeuille
from Connexion import Connexion
from Actifs import Actifs
import  random

class Portefeuille():

    ##il faut rajouter nbshares dans list actifs initialisé à 0

    def __init__(self, liste_Actifs, score):
        self.liste_Actifs = liste_Actifs
        self.score = score

    def Valeur_Portefeuille(self):
        #Fonction qui prend en argument un portefeuille et qui calcule
        #la valeur associée à ce portefeuille 
        liste_Actifs=self.liste_Actifs
        value=0
        for i in range(len(liste_Actifs)):
            #valeur=valeur asset*poids
            value = value + liste_Actifs[i].valeur*int(liste_Actifs[i].nb_shares)
        return value

    #Créé un portefeuil composé d'une liste d'action aléatoire
    def Creation_Portefeuille(self, MaxInvesti):

        liste_Actifs = self.liste_Actifs   
        prix_min = self.plus_petit_prix() 
        assets = list(range(len(liste_Actifs))) # liste des index de tous les actifs du portefeuille

        while (MaxInvesti > prix_min and len(assets) !=0 ):
        # Tant que la valeur a investir (MaxInvest) est superieur au prix de l'actif le moins cher
        # Et tant que la liste des index des actifs du portefeuil n'est pas vide
        # on ajoute une action au portefeuille

            # Selection aléatoire d'une action via son index dans la liste d'actif
            choice_asset = int(random.choice(assets))
            assets.remove(choice_asset) # On retire l'index de la liste pour ne pas tomber deux fois sur le même actif

            # Nombre maximal de shares que l'on peut acheter pour cet actif
            max_nb = MaxInvesti//(liste_Actifs[choice_asset].valeur)

            # Selection du nombre de shares entre 0 et nb_max 
            liste_Actifs[choice_asset].nb_shares = random.randint(0,max_nb)

            # On reduit la valeur a investir en lui retirant la valeur des parts de l'actif choisi
            MaxInvesti = MaxInvesti - liste_Actifs[choice_asset].nb_shares*liste_Actifs[choice_asset].valeur

        self.Poid_dans_portefeuille()
        return self

    # Calcul le prix de l'actif avec le plus faible 
    def plus_petit_prix(self):
        min = self.liste_Actifs[0].valeur
        for asset in self.liste_Actifs:
            if asset.valeur < min:
                min = asset.valeur
        return min 

    #Defini le poid qu'a l'action dans le portefeuille
    def Poid_dans_portefeuille(self):
        for i in range(len(self.liste_Actifs)):
            poids = self.liste_Actifs[i].valeur * self.liste_Actifs[i].nb_shares
            self.liste_Actifs[i].poids  = round(poids / self.Valeur_Portefeuille()*100,2)
        return self


    def __repr__(self):
        return "{0}\nValeur du portefeuil : {2}\nScore du portefeuille : {1}\n\n".format(self.liste_Actifs,self.score,self.Valeur_Portefeuille()) 