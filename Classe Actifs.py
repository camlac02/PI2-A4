  #Classe d'actifs

class Actif():
    def __init__(self, nom, valeur, volume, date):
        self.nom = nom
        self.valeur = valeur
        self.volume = volume
        self.date = date

    def creationActif(connexion):
        #Fonction qui prend en argument la connexion avec la base de données
        #La fonction retourne une liste d'actifs avec le nom de chaque actif
        liste_Actifs=[]
        return liste_Actifs

    def Valeur_Actif(liste_Actifs, date, connexion):
        #Fonction qui prend en arguments une liste d'actifs, la date du jour
        #et la connexion avec la base de données
        #La fonction retourne donc la liste des actifs qui correspondent au jour
        return liste_Actifs

    def __repr__(self):
        return "Nom : {0}, Valeur : {1}, Volume : {2}, Date : {3}\n".format(self.nom,self.valeur, self.volume, self.date) 