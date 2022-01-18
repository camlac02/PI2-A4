from django.http import request
from Connexion import Connexion

#Classe d'actifs

class Actifs():

    def __init__(self, nom, valeur, volume, date,nb_shares,rendement):
        self.nom = nom
        self.valeur = valeur
        self.volume = volume
        self.date = date
        self.nb_shares = nb_shares
        self.rendement = rendement
        #self.volatilité = 0

    def creationActifs(connexion):
        #Fonction qui prend en argument la connexion avec la base de données
        #La fonction retourne une liste d'actifs avec le nom de chaque actif 
        #Tout les autres attributs sont initialisée à 0     
        requete = 'Select distinct Noms from cac'
        curseur = connexion.execute(requete)
        liste_Actifs = []

        for row in curseur:
            action = Actifs(row['Noms'],0,0,0,0,0)
            liste_Actifs.append(action)
            
        return liste_Actifs


    def Valeur_Actifs(self, date, connection):
        #Fonction  qui prend en arguments une liste d'actifs, la date du jour
        #et la connexion avec la base de données
        #La fonction retourne une liste d'actifs, chacun asocié à une liste contenant
        #toutes les informations le concernant ('Noms', 'valeurs' et 'volumnes') à la date du jour 
        requete = "Select valeurs,volumes from cac where Dates = '"+date+"' and Noms = '"+str(self.nom)+"';"
        curseur = connection.execute(requete)
        row = curseur.fetchone()

        self.valeur = row['valeurs']
        self.volume = row['volumes']
        self.date = date
        self.Rendement_Actif(connection)

        return self
    
    
    def __repr__(self):
        #return "Nom : {0}, nbr d'action : {1}, r : {2};\n".format(self.nom,self.nb_shares,self.rendement)
        return "Nom : {0}, Valeur : {1}, Nbr d'Actions : {2}, \nDate : {3}\nRendement : {4}".format(self.nom,self.valeur, self.nb_shares, self.date,self.rendement)


    def Rendement_Actif(self,connexion):

        # Retourne une liste de tuple (date,rendement en %) d'un actif
        requete1 = "Select valeurs, Dates from cac where Noms = '"+self.nom+"';"
        curseur = connexion.execute(requete1)
        valeurs_precedente = 0 
  
        for row in curseur:
            if valeurs_precedente == 0:
                self.rendement = 0
            else :
                self.rendement = (round((row['valeurs'] - valeurs_precedente)/ valeurs_precedente *100,2))
            
            valeurs_precedente = row['valeurs']

        return self

    #.copy()

    ##################################  FONCTION PAS UTILISEE ################################################

    def copy(self):
        nom = self.nom
        valeur = self.valeur
        volume = self.volume
        date = self.date
        nb_shares = self.nb_shares.copy()
        rendement = self.rendement
        Actif = Actifs(nom,valeur,volume,date,nb_shares,rendement)
        return Actif

    def Rendement(connexion):

        requete_creation_columne = "ALTER TABLE cac ADD rendement float;"
        connexion.execute(requete_creation_columne)

        requete = "Select * from cac;"
        curseur = connexion.execute(requete)

        valeurs_precedente = 0 

        for row in curseur:

            requete2 = "INSERT INTO cac ('rendement') VALUES ("+ (round((row['valeurs'] - valeurs_precedente)/ valeurs_precedente *100,2)) +") ;"
            valeurs_precedente = row['valeurs']

        return 0 

'''
    def Volatilite_Actif(Nom_Actifs,connexion):
        
        r = Rendement_Actif(Nom_Actifs,connexion)
        r_moyen = 0 
        for i in range(len(r)):
            r_moyen = int(r[i]) + r_moyen     
        r_moyen = r_moyen / len(r)

        carre_ecart_variation_moyenne = []
        for i in r:
            carre_ecart_variation_moyenne.append((i-r_moyen)**2/100**2)

        v = 0

        for i in range(len(r)):
            v = v + carre_ecart_variation_moyenne[i]

        v = (v/len(r))**1/2

        return v


'''
    #############################################################################################################
