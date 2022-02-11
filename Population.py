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
            p = Portefeuille(list_asset,0,0).Creation_Portefeuille(MaxInvest)
            p.score_portefeuil()
            list_portefeuille.append(p)
        self.list_portefeuille = list_portefeuille
        return self
    
    #Tri les portefeuils d'une population en fonction de leurs scores
    def sort_population(self):

        for i in range(len(self.list_portefeuille)):
            for j in range(len(self.list_portefeuille)-1):
                if(self.list_portefeuille[j].score < self.list_portefeuille[j+1].score):
                    score = self.list_portefeuille[j].score
                    self.list_portefeuille[j].score = self.list_portefeuille[j+1].score
                    self.list_portefeuille[j+1].score = score
        return self

    def mutation(self):
        
        #Selectionner les portefeuilles a muter

        self.list_portefeuille[0].mutation()
        
        return self

    
    

    def __repr__(self):
        return "{0}".format(self.list_portefeuille)



