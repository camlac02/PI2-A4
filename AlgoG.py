from Portefeuille import Portefeuille 
from Population import Population
import random
from copy import deepcopy

class AlgoG() :

    def __init__(self, pop, generation_max):
        self.pop = pop
        self.generation_max = generation_max



    #On trie la population en fonction de son score en ordre descendant
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
                    final_list.append(list_portefeuille[j])
        self.pop.list_portefeuille = final_list
        return self



    def nouvelle_population(self,list_asset,MaxInvest,date_1,date_2,connexion):
    #Creation d'une nouvelle population en fonction d'une population précédente
        pop_precedente = self.pop    
       
        Pourcentage_garder = 0.5 #Pourcentage de la population précédente à muter et croiser
        new_list_portefeuille = []
        new_list_portefeuille.append(pop_precedente.list_portefeuille[0]) #On garde le portefeuille avec le meilleur score.

        for i in range(1,len(pop_precedente.list_portefeuille)):
            
            
            if i < len(pop_precedente.list_portefeuille)*Pourcentage_garder:
                #On croise et mute le pourcentage de la population choisit

                rnd = round(random.uniform(1,2)) #Une chance sur deux de croiser et une chance sur deux de muter
                if rnd == 1:
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest,date_1,date_2,connexion))
                    #new_list_portefeuille.append(pop_precedente.crossover(MaxInvest))
                if rnd == 2: 
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest,date_1,date_2,connexion))
                    #new_list_portefeuille.append(pop_precedente.crossover(MaxInvest))
            else :
                #On complete la population avec des portefeuilles crées aléatoirement
                new_list_portefeuille.append(Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest,date_1,date_2,connexion))

        return new_list_portefeuille 



    # fonction executant l'algorithme genetique
    def algorihtme_genetique(self, liste_assets, max_invest, exp_ret, exp_vol,date_1,date_2,connexion):
        generation = 0
        while generation <= self.generation_max : #'''((self.pop.list_portefeuille[0].rendement < 0.8*exp_ret) or (self.pop.list_portefeuille[0].volatilite > exp_vol)) and'''

            print('\nGeneration : '+str(generation)+'\n')
            self.pop = Population(self.nouvelle_population(liste_assets,max_invest,date_1,date_2,connexion))
            self.sort_population()

            print('\n',self.pop.__repr__())
            generation += 1

        return self.pop.list_portefeuille[0]

