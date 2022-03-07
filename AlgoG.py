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
                if rnd == 2: 
                    new_list_portefeuille.append(pop_precedente.list_portefeuille[i].mutation(MaxInvest))
                    #new_list_portefeuille.append(pop_precedente.crossover(MaxInvest)
            else :
                new_list_portefeuille.append(Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest))

        return new_list_portefeuille 

    # fonction de mutation de portefeuille 
    def mutation_portefeuille(self,index,MaxInvest):

        self.pop.list_portefeuille[index].mutation(MaxInvest)  
        return self

    # fonction executant l'algorithme genetique
    def algorihtme_genetique(self, liste_assets, max_invest,rendement_attendu):
        generation = 0
        self.pop.list_portefeuille[0].rendement = 0

        while generation < self.generation_max and rendement_attendu != self.pop.list_portefeuille[0].rendement :

            print('\nGeneration : '+str(generation)+'\n')
            self.pop = Population(self.nouvelle_population(liste_assets,max_invest))
            self.sort_population()

            print('\n',self.pop.__repr__())
            generation += 1

        return self.pop.list_portefeuille[0]

##################################################################################################################### A REGARDER

    def crossover(self, max_invest):
        alpha=0.25*max_invest #pourcentage d'échnage des portefeuilles lors du crossover  (/!\ Peut etre le passé en parametre pour le client)
        list_trie=self.sort_population
        parent1=list_trie[0]
        parent2=list_trie[-1]
        mut1=Portefeuille([],0,0,0,0)
        mut2=Portefeuille([],0,0,0,0)
        while mut1.Valeur_Portefeuille <alpha: #Trouver une solution pour tomber exactement sur le max invest, ce faire une marge sur le pourcentage effectué pour ne pas dépasser ?
            mut1.liste_Actifs.append(parent1.liste_Actifs.pop())
        while mut2.Valeur_Portefeuille <alpha:
            mut2.liste_Actifs.append(parent2.liste_Actifs.pop())
        new_parent1=parent1+mut2
        new_parent2=parent2+mut1
        #remplacement des anciens portefeuilles par les nouveaux(ou seulement ajout des nouveaux si on le souhaite)
        list_trie.pop()
        list_trie.pop(0)
        list_trie.append(new_parent1)
        list_trie.append(new_parent2)
        self=list_trie
        return self
    

