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
        reste_a_investir = MaxInvesti

        while (MaxInvesti > self.Valeur_Portefeuille()):

            # Selection d'une action
            choice_asset = random.randint(0,len(liste_Actifs)-1)

            # Nombre maximal de shares supportable de cet actif
            max_nb = reste_a_investir//(liste_Actifs[choice_asset].valeur)

            # Selection du nombre de shares entre 0 et nb_max
            nb_shares = random.randint(0,max_nb)
            liste_Actifs[choice_asset].nb_shares = nb_shares

            reste_a_investir = reste_a_investir - nb_shares*liste_Actifs[choice_asset].valeur

        self.Poid_dans_portefeuille()
        return self

    def Depasse_MaxInvesti(self):
        depasse = False


        return depasse

    #Defini le poid qu'a l'action dans le portefeuil
    def Poid_dans_portefeuille(self):
        for i in range(len(self.liste_Actifs)):
            poids = self.liste_Actifs[i].valeur * self.liste_Actifs[i].nb_shares
            self.liste_Actifs[i].poids  = round(poids / self.Valeur_Portefeuille()*100,2)
        return self

    def __repr__(self):
        return "{0}\nValeur du portefeuil : {2}\nScore du portefeuille : {1}\n\n".format(self.liste_Actifs,self.score,self.Valeur_Portefeuille()) 