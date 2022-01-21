from Connexion import Connexion
import pandas
from math import nan
from django.http import request


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
        requete = 'Select distinct name from helo'
        curseur = connexion.execute(requete)
        liste_Actifs = []

        for row in curseur:
            action = Actifs(row['name'],0,0,0,0,0)
            liste_Actifs.append(action)
            
        return liste_Actifs


    def Valeur_Actifs(self, date, connection):
        #Fonction  qui prend en arguments une liste d'actifs, la date du jour
        #et la connexion avec la base de données
        #La fonction retourne une liste d'actifs, chacun asocié à une liste contenant
        #toutes les informations le concernant ('name', 'value' et 'volumnes') à la date du jour 
        requete = "Select value,volume,Rendements from helo where date = '"+date+"' and name = '"+str(self.nom)+"';"
        curseur = connection.execute(requete)
        row = curseur.fetchone()

        self.valeur = row['value']
        self.volume = row['volume']
        self.date = date
        self.rendement=row['Rendements']

        return self
    
    
    def __repr__(self):
        #return "Nom : {0}, nbr d'action : {1}, r : {2};\n".format(self.nom,self.nb_shares,self.rendement)
        return "Nom : {0}, Valeur : {1}, Nbr d'Actions : {2}, \nDate : {3}\nRendement : {4}".format(self.nom,self.valeur, self.nb_shares, self.date,self.rendement)


    def Rendement_Actif(self,connexion):

        # Retourne une liste de tuple (date,rendement en %) d'un actif
        requete1 = "Select value, date from helo where name = '"+self.nom+"';"
        curseur = connexion.execute(requete1)
        valeurs_precedente = 0 
  
        for row in curseur:
            if valeurs_precedente == 0:
                self.rendement = 0
            else :
                self.rendement = (round((row['value'] - valeurs_precedente)/ valeurs_precedente *100,2))
            
            valeurs_precedente = row['value']

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

        requete_creation_columne = "ALTER TABLE helo ADD rendement float;"
        connexion.execute(requete_creation_columne)

        requete = "Select * from cac;"
        curseur = connexion.execute(requete)

        valeurs_precedente = 0 

        for row in curseur:

            requete2 = "INSERT INTO cac ('rendement') VALUES ("+ (round((row['value'] - valeurs_precedente)/ valeurs_precedente *100,2)) +") ;"
            valeurs_precedente = row['value']

        return 0 

    #############################################################################################################

    #fonction pour introduire les rendements dans un csv
'''
    def InsertionRendements(connexion):
        requete1="Select distinct name from helo;"
        curseur=connexion.execute(requete1)
        ListeNoms=[]
        #on récupère la liste des noms des actifs
        for row in curseur:
            ListeNoms.append(row['name'])
        for i in ListeNoms:
            print(i)
        ListeRendements=[]
        for name in ListeNoms:
            requete2="select value,date from helo where name='"+name+"';"
            #on récupère la liste des value de chaque actif
            
            #ListeRendements[1]=0; #on met le premier à 0
            ListeValeurs=[]
            curseur2=connexion.execute(requete2)
            for row in curseur2:
                ListeValeurs.append(row['value'])
            print(len(ListeValeurs))
            ListeDates=[]
            for row in curseur2:
                ListeDates.append(row['date'])
            #ListeRendements=[len(ListeValeurs)]
            for i in range(0,len(ListeValeurs)-1):
                ListeRendements.append(ListeValeurs[i+1]/ListeValeurs[i]-1)
            ListeRendements.append(nan)
        #print("taille :",len(ListeRendements))
        #print(ListeRendements)
        #print(name)
        #requete3="""update helo set Rendement =1"""
        #connexion.execute(requete3)

        data=pandas.read_csv('/Users/heloisemalcles/Desktop/ESILV A4/Pi2/DonneesActifs.csv',sep=";")
        print(data)
        data=pandas.DataFrame(data)
        data2=data.assign(Rendements=nan)
        print(data2)
        #data2['Rendements'][1]=0
        for i in range(0,len(ListeRendements)):
            data2['Rendements'][i]=ListeRendements[i]
        
        print(data2)

        data2.to_csv("/Users/heloisemalcles/Desktop/ESILV A4/Pi2/dataTesteHelo.csv",index=False,sep=";")

'''