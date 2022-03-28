#Classe d'actifs
class Actifs():

    def __init__(self, nom, valeur, volume, date, nb_shares ,rendement, poids, ListeRendementsValeurs):
        self.nom = nom
        self.valeur = valeur
        self.volume = volume
        self.date = date
        self.nb_shares = nb_shares
        self.rendement = rendement
        self.poids=poids 
        self.ListeRendementsValeurs=ListeRendementsValeurs

    def creationActifs(connexion):
        #Fonction qui prend en argument la connexion avec la base de données
        #La fonction retourne une liste d'actifs avec le nom de chaque actif 
        #Tout les autres attributs sont initialisée à 0     
        requete = 'Select distinct name from cac'
        curseur = connexion.execute(requete)
        liste_Actifs = []

        for row in curseur:
            action = Actifs(row['name'],0,0,0,0,0,0,0)
            liste_Actifs.append(action)
            
        return liste_Actifs

    def Valeur_Actifs(self, date1, date2, connection):
        #Fonction  qui prend en arguments une liste d'actifs, la date du jour (date1), 
        #la date jusqu'à laquelle on souhaite etudier la performance de l'actif (date2)
        #et la connexion avec la base de données

        #La fonction retourne une liste d'actifs, chacun asocié à une liste contenant
        #toutes les informations le concernant
        requete = "Select value,volume,Rendements from cac where date = '"+date1+"' and name = '"+str(self.nom)+"';"
        curseur = connection.execute(requete)
        row = curseur.fetchone()
        
        self.valeur = row['value']
        self.volume = row['volume']
        self.date = date1
        self.rendement=row['Rendements']
        self.poids=0
        self.RendementsPourPF(date1,date2,connection)
        
        return self
    
    #Creation d'une liste de (rendements actif,valeur actif) par jour pour un actif sur la période donnée (date1 à date2)
    def RendementsPourPF(self,date1,date2,connection):
        Liste=[]
        requete2="select Rendements,value from cac where name='"+str(self.nom)+"' and date between '"+date1+"' and '"+date2+"';"
        #on récupère la liste des Rendements de chaque actif
        curseur2=connection.execute(requete2)    
        for row in curseur2:
            Liste.append([row['Rendements'],row['value']])

        #On ajoute la liste (rendements,valeur) aux parametres de l'actif
        self.ListeRendementsValeurs=Liste

    #Fonction qui retourne les informations concernant une action sous forme de chaine de caratères
    def __repr__(self):
        return "Nom : {0}, Valeur : {1}, Nbr d'Actions : {2}, \nDate : {3}\n".format(self.nom,self.valeur, self.nb_shares, self.date)
