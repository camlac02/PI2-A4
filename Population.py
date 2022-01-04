from Portefeuille import Portefeuille 
from Actifs import Actifs

class Population() :

    def __init__(self, list_portefeuille):
        self.list_portefeuille = list_portefeuille


    def Creation_Population(self, nb_portefeuille, MaxInvesti,list_asset_with_value): #Paramètres à ajouter selon condition du client ? 
        for i in range(nb_portefeuille):
            print(i)
            self.list_portefeuille[i] = Portefeuille(list_asset_with_value,0).Creation_Portefeuille(MaxInvesti)   
        
        return self

    def __repr__(self):
        return "{0}".format(self.list_portefeuille)



