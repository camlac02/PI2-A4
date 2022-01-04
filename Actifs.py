from Connexion import Connexion

#Classe d'actifs

class Actifs():

    def __init__(self, nom, valeur, volume, date,nb_shares):
        self.nom = nom
        self.valeur = valeur
        self.volume = volume
        self.date = date
        self.nb_shares = nb_shares
        #self.rendement = 0
        #self.volatilité = 0

    def creationActifs(connexion):
        #Fonction qui prend en argument la connexion avec la base de données
        #La fonction retourne une liste d'actifs avec le nom de chaque actif 
        #Tout les autres attributs sont initialisée à 0     
        requete = 'Select distinct Noms from cac'
        curseur = connexion.execute(requete)
        liste_Actifs = []

        for row in curseur:
            action = Actifs(row['Noms'],0,0,0,0)
            liste_Actifs.append(action)
            
        return liste_Actifs


    def Valeur_Actifs(self, date, connexion):
        #Fonction  qui prend en arguments une liste d'actifs, la date du jour
        #et la connexion avec la base de données
        #La fonction retourne une liste d'actifs, chacun asocié à une liste contenant
        #toutes les informations le concernant ('Noms', 'valeurs' et 'volumnes') à la date du jour 
        requete = "Select valeurs,volumes from cac where Dates = '"+date+"' and Noms = '"+str(self.nom)+"';"
        curseur = connexion.execute(requete)
        row = curseur.fetchone()

        self.valeur = row['valeurs']
        self.volume = row['volumes']
        self.date = date

        return self
    
    
    def __repr__(self):
        #return "Nom : {0}, Valeur : {1}, Volume : {2}, Date : {3}\n".format(self.nom,self.valeur, self.volume, self.date)
        #return "Nom : {0}, Valeur : {1}, Date : {2}\n".format(self.nom,self.valeur, self.date)
        return "Nom : {0}, Valeur : {1}, Nbr d'Actions : {2}, \nDate : {3}".format(self.nom,self.valeur, self.nb_shares, self.date)

    
    ##################################  FONCTION PAS UTILISEE ################################################
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
    #############################################################################################################

