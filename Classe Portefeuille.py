#Classe Portefeuille

class Portefeuille():

    def __init__(self, liste_Actifs, score):
        self.liste_Actifs = liste_Actifs
        self.score = score

    def Valeur_Portefeuille(self):
        #Fonction qui prend en argument un portefeuille et qui calcule
        #la valeur associée à ce portefeuille suivant les poids de chaque actif*
        #La fonction retourne la valeur de l'entier
        valeur = 0
        return valeur

    def Creation_Portefeuille(self, MaxInvesti):
        #Fonction qui prend en argument un portefeuille et un entier qui
        #représente la valeur investie
        #La fonction retourne un portefeuille qui associe des valeurs aléatoires
        #de poids à chaque actif
        return self

    def __repr__(self):
        return "{0}\nScore du portefeuille : {1}\n\n".format(self.liste_Actifs,self.score) 
