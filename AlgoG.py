from Portefeuille import Portefeuille 
from Actifs import Actifs
from Population import Population
import random

class AlgoG() :

    #Attributs
    def __init__(self, pop, generation_max):
        self.pop = pop
        self.generation_max = generation_max


    #Tri de la population
    def sort_population(self):

        list_portefeuille = self.pop.list_portefeuille

        for i in range(len(list_portefeuille)):
            for j in range(len(list_portefeuille)-1):
                if(list_portefeuille[j].score < list_portefeuille[j+1].score):
                    score = list_portefeuille[j].score
                    list_portefeuille[j].score = list_portefeuille[j+1].score
                    list_portefeuille[j+1].score = score
        return self

    #Creation d'une nouvelle population à partir de la précédente
    def nouvelle_population(self,list_asset,MaxInvest):
        
        pop_precedente = self.pop

        Pourcentage_garder = 0.5
        new_list_portefeuille = []

        # Ajout du portefeuille avec le meilleur score dans la nouvelle liste de portefeuilles
        new_list_portefeuille.append(pop_precedente.list_portefeuille[0])

        for i in range(1,len(pop_precedente.list_portefeuille)):
            
            if i < len(pop_precedente.list_portefeuille)*Pourcentage_garder:

                rnd = round(random.uniform(1,2))
                #Ajout de portefeuilles obtenus par mutations et croisements
                if rnd == 1:
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest))
                if rnd == 2: 
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest))
                    #new_list_portefeuille.append(pop_precedente.crossover(MaxInvest))
            else :
                new_list_portefeuille.append(Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest))

            #new_list_portefeuille[i].RatioSharpe() #Marche pas

        return new_list_portefeuille 
    
    

    def crossover(self):
    
        return self


    #Fonction de mutation de portefeuille 
    def mutation_portefeuille(self,index,MaxInvest):

        self.pop.list_portefeuille[index].mutation(MaxInvest)  
        return self

    #Fonction executant l'algorithme genetique
    def algorihtme_genetique(self, liste_assets, max_invest):

        for i in range(self.generation_max):

            print('\nGeneration : '+str(i)+'\n')
            self.pop = Population(self.nouvelle_population(liste_assets,max_invest))
            self.sort_population()

            print(self.pop.__repr__())

        return self.pop.list_portefeuille[0]