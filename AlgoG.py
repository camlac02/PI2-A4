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

        i = 1
        while i < len(pop_precedente.list_portefeuille):
            
            
            if i < 2:#len(pop_precedente.list_portefeuille)*Pourcentage_garder:
                #On croise et mute le pourcentage de la population choisit

                rnd = round(random.uniform(1,2)) #Une chance sur deux de croiser et une chance sur deux de muter
                if rnd == 1:
                    print('\nCROSSOVER\n')
                    cross = Population.crossover(pop_precedente.list_portefeuille[i],pop_precedente.list_portefeuille[i+1],date_1,date_2,connexion)
                    new_list_portefeuille.append(cross[0])
                    new_list_portefeuille.append(cross[1])
                    i+=2
                if rnd == 2: 
                    print('\nMUTATION\n')
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest,date_1,date_2,connexion))
                    i+=1           
            else :
                #On complete la population avec des portefeuilles crées aléatoirement
                new_list_portefeuille.append(Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest,date_1,date_2,connexion))
                i +=1

        return new_list_portefeuille 



    #Fonction executant l'algorithme genetique en fonction des conditions d'objectifs de rendement et de volatilité posés par l'utilisateur
    def algorihtme_genetique(self, liste_assets, max_invest, exp_ret, exp_vol,date_1,date_2,connexion):
        generation = 0

        self.sort_population()

        if (exp_ret == 0):
            if (exp_vol == 0):
            #Si aucun rendement ou volatilité n'est entré par l'utilisateur.
                while generation <= self.generation_max:
    
                    self.Generation(liste_assets, max_invest, generation, date_1,date_2,connexion)
                    generation += 1

                return self.pop.list_portefeuille[0]

            #Si aucun rendement n'est entré par l'utilisateur (mais l'utilisateur à rentré une volatilité).
            else : 
                while generation <= self.generation_max and (self.pop.list_portefeuille[0].volatilite < 0.9*exp_vol or self.pop.list_portefeuille[0].volatilite > 1.1*exp_vol):
        
                    self.Generation(liste_assets, max_invest, generation, date_1,date_2,connexion)
                    generation += 1

                return self.pop.list_portefeuille[0]
        else:
            if (exp_vol == 0):
            #Si aucune volatilité n'est entré par l'utilisateur (mais l'utilisateur à rentré un rendement)
                while generation <= self.generation_max and (self.pop.list_portefeuille[0].rendement < 0.9*exp_ret):
            
                    self.Generation(liste_assets, max_invest, generation, date_1,date_2,connexion)
                    generation += 1

                return self.pop.list_portefeuille[0]
            else :
            #Si un rendement et une volatilité sont entré par l'utilisateur.
                while generation <= self.generation_max and ((self.pop.list_portefeuille[0].rendement < 0.9*exp_ret) or (self.pop.list_portefeuille[0].volatilite < 0.9*exp_vol or self.pop.list_portefeuille[0].volatilite > 1.1*exp_vol)):

                    self.Generation(liste_assets, max_invest, generation, date_1,date_2,connexion)
                    generation += 1

                return self.pop.list_portefeuille[0]



    #Crée la nouvelle population pour chaque génération
    def Generation(self, liste_assets, max_invest, generation, date_1,date_2,connexion):

            print('\n############## Generation : '+str(generation)+' ##############\n')
            self.pop = Population(self.nouvelle_population(liste_assets,max_invest,date_1,date_2,connexion))
            self.sort_population()

            print('\n',self.pop.__repr__())
            


