# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:00:09 2022

@author: PC
"""
from Portefeuille import Portefeuille 
from Actifs import Actifs
from Connexion import Connexion
import random

class Population() :

    def __init__(self, list_portefeuille):
        self.list_portefeuille = list_portefeuille

    def Creation_Population(self, list_asset, MaxInvest, nb_portefeuille):
        
        list_portefeuille = []

        for i in range(nb_portefeuille):
            

            p = Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest)
            list_portefeuille.append(p)

        self.list_portefeuille = list_portefeuille
        
        return self
    
    #Calcul des rendements moyens entre 2 dates

     #Tri les portefeuils d'une population en fonction de leurs scores
    def sort_population(self):

        for i in range(len(self.list_portefeuille)):
            for j in range(len(self.list_portefeuille)-1):
                if(self.list_portefeuille[j].score < self.list_portefeuille[j+1].score):
                    score = self.list_portefeuille[j].score
                    self.list_portefeuille[j].score = self.list_portefeuille[j+1].score
                    self.list_portefeuille[j+1].score = score
        return self

    # def mutation_portefeuille(self,index,MaxInvest):

    #     self.list_portefeuille[index].mutation(MaxInvest)
    #     return self

    def crossover(self):

        return self


    def nouvelle_population(pop_precedente,list_asset,MaxInvest):
        
        Pourcentage_garder = 0.5
        new_list_portefeuille = []

        new_list_portefeuille.append(pop_precedente.list_portefeuille[0])

        for i in range(1,len(pop_precedente.list_portefeuille)):
            
            if i < len(pop_precedente.list_portefeuille)*Pourcentage_garder:

                rnd = round(random.uniform(1,2))

                if rnd == 1:
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest))
                if rnd == 2: 
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest))
                    #new_list_portefeuille.append(pop_precedente.mutation_portefeuille(MaxInvest).list_portefeuille)
            else :
                new_list_portefeuille.append(Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest))

            new_list_portefeuille[i].RatioSharpe()

        return new_list_portefeuille 

    def __repr__(self):
        return "{0}".format(self.list_portefeuille)

if __name__=="__main__":
    pop = Population ([])
    connection = Connexion('BDD','root','PetruLuigi0405@!')
    connection.initialisation()
    'pop.MoyenneRendements(connection,"2017-11-09","2017-11-17")'
    connection.close_connection()
