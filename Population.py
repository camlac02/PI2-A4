#from multiprocessing import Value
from Portefeuille import Portefeuille 
from Actifs import Actifs
import random

class Population() :

    def __init__(self, list_portefeuille):
        self.list_portefeuille = list_portefeuille

    def creation_population(self, list_asset, MaxInvest, nb_portefeuille):
        list_portefeuille = []
        for i in range(nb_portefeuille):
            p = Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest)
            list_portefeuille.append(p)
        self.list_portefeuille = list_portefeuille
        return self
    
    def __repr__(self):
        return "\nPopulation : {0}".format(self.list_portefeuille)



