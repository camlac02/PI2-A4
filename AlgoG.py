# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:54:24 2022

@author: PC
"""

from Portefeuille import Portefeuille 
from Actifs import Actifs
from Population import Population
import random
from copy import deepcopy

class AlgoG() :

    def __init__(self, pop, generation_max):
        self.pop = pop
        self.generation_max = generation_max


    #Sort population
    def sort_population(self):
        list_score=[]
        list_portefeuille = deepcopy(self.pop.list_portefeuille)
        for i in range(len(list_portefeuille)):
            list_score.append(list_portefeuille[i].score)
        list_score = sorted(list_score,reverse=True)

        final_list = []
        for i in range(len(list_score)):
            for j in range(len(list_portefeuille)):
                if(list_portefeuille[j].score == list_score[i]):
                    print(list_score[i])
                    final_list.append(list_portefeuille[j])
        self.pop.list_portefeuille = final_list
        return self


    #Cree une nouvelle population a partir de la precedente
    def nouvelle_population(self,list_asset,MaxInvest):
        
        pop_precedente = self.pop

        Pourcentage_garder = 0.5
        new_list_portefeuille = []

        new_list_portefeuille.append(pop_precedente.list_portefeuille[0])

        for i in range(1,len(pop_precedente.list_portefeuille)):
            
            if i < len(pop_precedente.list_portefeuille)*Pourcentage_garder:

                rnd = round(random.uniform(1,2))
                if rnd == 1:
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest))
                    #new_list_portefeuille.append(pop_precedente.crossover(MaxInvest))
                if rnd == 2: 
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest))
                    #new_list_portefeuille.append(pop_precedente.crossover(MaxInvest))
            else :
                new_list_portefeuille.append(Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest))
            #new_list_portefeuille.append(Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest))
        return new_list_portefeuille 

    # # fonction de mutation de portefeuille 
    # def mutation_portefeuille(self,index,MaxInvest):

    #     self.pop.list_portefeuille[index].mutation(MaxInvest)  
    #     return self

    # fonction executant l'algorithme genetique
    def algorihtme_genetique(self, liste_assets, max_invest, exp_ret, exp_vol):
        generation = 0
        while generation <= self.generation_max : #'''((self.pop.list_portefeuille[0].rendement < 0.8*exp_ret) or (self.pop.list_portefeuille[0].volatilite > exp_vol)) and'''

            print('\nGeneration : '+str(generation)+'\n')
            self.pop = Population(self.nouvelle_population(liste_assets,max_invest))
            self.sort_population()

            print('\n',self.pop.__repr__())
            generation += 1

        return self.pop.list_portefeuille[0]

