from Portefeuille import Portefeuille 
from Actifs import Actifs

class Population() :

    def __init__(self, list_portefeuille):
        self.list_portefeuille = list_portefeuille


    def Creation_Population(nb_portefeuille, MaxInvesti,list_asset_with_value): # Paramètres à ajouter
        list_portefeuille = []
        for i in range(0,nb_portefeuille-1):
            print(i)
            list_portefeuille[i] = Portefeuille(list_asset_with_value,0).Creation_Portefeuille(MaxInvesti)     
        return list_portefeuille

    def __repr__(self):
        return "{0}".format(self.list_portefeuille)


