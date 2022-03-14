from Portefeuille import Portefeuille 
from Actifs import Actifs
from Population import Population
import random

class AlgoG() :

    def __init__(self, pop, generation_max):
        self.pop = pop
        self.generation_max = generation_max


    #Sort population
    def sort_population(self):

        list_portefeuille = self.pop.list_portefeuille

        for i in range(len(list_portefeuille)):
            for j in range(len(list_portefeuille)-1):
                if(list_portefeuille[j].score < list_portefeuille[j+1].score): 
                    score = list_portefeuille[j].score
                    list_portefeuille[j].score = list_portefeuille[j+1].score
                    list_portefeuille[j+1].score = score

        # final_list = []
        # for i in range(len(list_score)):
        #     for j in range(len(list_portefeuille)):
        #         if(list_portefeuille[j].score == list_score[i]):
        #             final_list.append(list_portefeuille[j])
        # self.pop.list_portefeuille = final_list
        # return self

    #Cree une nouvelle population a partir de la precedente
    def nouvelle_population(self,list_asset,MaxInvest):
        
        pop_precedente = self.pop

        Pourcentage_garder = 0.4
        new_list_portefeuille = []

        new_list_portefeuille.append(pop_precedente.list_portefeuille[0])

        count = 1
        while count < len(pop_precedente.list_portefeuille):
        #for i in range(1,len(pop_precedente.list_portefeuille)):
            
            if len(new_list_portefeuille) < len(pop_precedente.list_portefeuille)*Pourcentage_garder:

                rnd = round(random.uniform(1,2))

                if rnd == 1:
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[count].mutation(MaxInvest))
                    # pop = pop_precedente.crossover(MaxInvest,count)
                    # # print(pop[0].liste_Actifs)
                    # # print(pop[1].liste_Actifs)
                    # new_list_portefeuille.append(pop[0])
                    # new_list_portefeuille.append(pop[1])
                    #count +=1
                if rnd == 2: 
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[count].mutation(MaxInvest))
                    # pop = pop_precedente.crossover(MaxInvest,count)
                    # # print(pop[0].liste_Actifs)
                    # # print(pop[1].liste_Actifs)
                    # new_list_portefeuille.append(pop[0])
                    # new_list_portefeuille.append(pop[1])
                    #count +=1
            else :
                new_list_portefeuille.append(Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest))
            count+=1

        return new_list_portefeuille 

    # # fonction de mutation de portefeuille 
    # def mutation_portefeuille(self,index,MaxInvest):

    #     self.pop.list_portefeuille[index].mutation(MaxInvest)  
    #     return self

    # fonction executant l'algorithme genetique
    def algorihtme_genetique(self, liste_assets, max_invest):
        generation = 0

        while generation < self.generation_max :

            print('\nGeneration : '+str(generation)+'\n')
            self.pop = Population(self.nouvelle_population(liste_assets,max_invest))
            #print('\navant sort',self.pop.__repr__())
            self.sort_population()

            print('\napres sort',self.pop.__repr__())
            generation += 1

        return self.pop.list_portefeuille[0]

##################################################################################################################### A REGARDER

   
    

