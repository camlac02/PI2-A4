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
        size = len(liste_Actifs)
        i=0
        while i<size:
            #valeur=valeur asset*poids
            value = value + liste_Actifs[i].value*int(liste_Actifs[i].nb_shares)
            i=i+1
        return value

    def Creation_Portefeuille(self, MaxInvesti):
        #cette fonction prend en parametre un investissement max
        #retourne un portefeuille qui respecte les conditions initiales
        liste_Actifs = self.liste_Actifs
        i=0
        size= len(liste_Actifs)
        while(self.Valeur_Portefeuille()<MaxInvesti):
            #On prend des actions parmi notre liste d'actifs
            choice_assets= random.randint(0,len(liste_Actifs)-1)
            #On choisit de maniere random le nombre de shares par actions tout en prenant en compte l'investissement max
            max_value = MaxInvesti//((liste_Actifs[choice_assets].valeur)*(size/2))
            nb_shares = random.randint(0,max_value)
            liste_Actifs[choice_assets].nb_shares=nb_shares
        i=0
        while i<len(liste_Actifs):
            poids = liste_Actifs[i].value * liste_Actifs[i].nb_shares
            volume = poids/self.Valeur_Portefeuille()
            self.liste_Actifs[i].volume=volume #cela correspond a la valeur d'un actif*nb shares/valeur du portefeuille
            i=i+1
        return self

    def __repr__(self):
        return "{0}\nScore du portefeuille : {1}\n\n".format(self.liste_Actifs,self.score) 