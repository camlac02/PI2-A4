from Connexion import Connexion

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
        
        requete = 'Select distinct Noms from cac'
        curseur = connexion.execute(requete)
        liste_Actifs = []

        for row in curseur:
             liste_Actifs.append(row)

        return liste_Actifs

    def Valeur_Actif(liste_Actifs, date, connexion):

        #Fonction qui prend en arguments une liste d'actifs, la date du jour
        #et la connexion avec la base de données
        #La fonction retourne une liste d'actifs, chacun asocié à une liste contenant
        #toutes les informations le concernant ('Noms', 'valeurs' et 'volumnes') à la date du jour 

        for i in range(len(liste_Actifs)):
            actif = []

            requete = "Select Noms, Valeurs, Volumes from cac where Dates = '"+date+"' and Noms = '"+liste_Actifs[i]['Noms']+"';"

            curseur = connexion.execute(requete)

            for row in curseur:
                actif.append(row)
            liste_Actifs[i] = actif

        return liste_Actifs

    def __repr__(self):
        return "Nom : {0}, Valeur : {1}, Volume : {2}, Date : {3}\n".format(self.nom,self.valeur, self.volume, self.date)
