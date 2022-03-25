from Portefeuille import Portefeuille 

#Classe Population
class Population() :

    def __init__(self, list_portefeuille):
        self.list_portefeuille = list_portefeuille


    
    def creation_population(self, list_asset, MaxInvest, nb_portefeuille,date_1,date_2,connexion):
    #Creation de la population en fonction du nombre de portefeuille voulu.
        list_portefeuille = []
        for i in range(nb_portefeuille):
            #Creation de chaque portefeuille de la population
            p = Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest,date_1,date_2,connexion)
            list_portefeuille.append(p) #On ajoute le portefeuille à la liste de portefeuille qui va composer la population

        self.list_portefeuille = list_portefeuille
        return self



    #Retourne une chaine de caractère contenant la liste de portefeuilles contenu dans une population.
    def __repr__(self):
        return "{0}".format(self.list_portefeuille)

