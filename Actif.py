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
            action = Actif(row['Noms'],0,0,0)
            liste_Actifs.append(action)
        return liste_Actifs

    def Valeur_Actif(liste_Actifs, date, connexion):

        #Fonction qui prend en arguments une liste d'actifs, la date du jour
        #et la connexion avec la base de données
        #La fonction retourne une liste d'actifs, chacun asocié à une liste contenant
        #toutes les informations le concernant ('Noms', 'valeurs' et 'volumnes') à la date du jour 

        for i in range(len(liste_Actifs)):

            requete = "Select valeurs,volumes from cac where Dates = '"+date+"' and Noms = '"+str(liste_Actifs[i].nom)+"';"

            curseur = connexion.execute(requete)

            row = curseur.fetchone()

            liste_Actifs[i].valeur = row['valeurs']
            liste_Actifs[i].volume = row['volumes']
            liste_Actifs[i].date = date

        return liste_Actifs
    
    
    def Rendement_Actif(Nom_Actifs,connexion):

        # Retourne une liste de tuple (date,rendement en %) d'un actif

        requete1 = "Select valeurs, Dates from cac where Noms = '"+Nom_Actifs+"';"
        curseur = connexion.execute(requete1)
        valeurs_precedente = 0 
        r = []

        for row in curseur:
            if valeurs_precedente == 0:
                r.append(0)
            else :
                r.append((row['Dates'].strftime("%d/%m/%Y"),round((row['valeurs'] - valeurs_precedente)/ valeurs_precedente *100,2)))
            valeurs_precedente = row['valeurs']
            
        return r


    def __repr__(self):
        return "Nom : {0}, Valeur : {1}, Volume : {2}, Date : {3}\n".format(self.nom,self.valeur, self.volume, self.date)

