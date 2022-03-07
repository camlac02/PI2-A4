#from multiprocessing import Value
from Portefeuille import Portefeuille 
from Actifs import Actifs
import random
from Fitness import fitness

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


    def crossover(self, max_invest):
        alpha=0.25*max_invest #pourcentage d'échnage des portefeuilles lors du crossover  (/!\ Peut etre le passé en parametre pour le client)
        list_trie = self.list_portefeuille
        parent1 = list_trie[1]
        parent2= list_trie[-1]
        mut1=Portefeuille([],0,0,0,0)
        mut2=Portefeuille([],0,0,0,0)
        while mut1.Valeur_Portefeuille().valeur < alpha: #Trouver une solution pour tomber exactement sur le max invest, ce faire une marge sur le pourcentage effectué pour ne pas dépasser ?
            mut1.liste_Actifs.append(parent1.liste_Actifs.pop())
        while mut2.Valeur_Portefeuille().valeur <alpha:
            mut2.liste_Actifs.append(parent2.liste_Actifs.pop())
        new_parent1 = parent1.liste_Actifs + mut2.liste_Actifs
        new_parent2 = parent2.liste_Actifs + mut1.liste_Actifs
        #remplacement des anciens portefeuilles par les nouveaux(ou seulement ajout des nouveaux si on le souhaite)
        list_trie.pop()
        list_trie.pop(0)
        list_trie.append(new_parent1)
        list_trie.append(new_parent2)
        self.list_portefeuille = list_trie
        self.__repr__()

        liste_Actif = self.list_portefeuille[1].liste_Actifs
        self.list_portefeuille[1].Valeur_Portefeuille()
        self.list_portefeuille[1].Poid_dans_portefeuille() # calcule la valeur finale du portefeuille
        self.list_portefeuille[1].VolPortefeuille(liste_Actif)
        self.list_portefeuille[1].RendementsPF(liste_Actif)
        fit = fitness(self.list_portefeuille[1], 0) 
        self.list_portefeuille[1].score = fit.RatioSharpe()

        liste_Actif = self.list_portefeuille[0].liste_Actifs
        self.list_portefeuille[0].Valeur_Portefeuille()
        self.list_portefeuille[0].Poid_dans_portefeuille() # calcule la valeur finale du portefeuille
        self.list_portefeuille[0].VolPortefeuille(liste_Actif)
        self.list_portefeuille[0].RendementsPF(liste_Actif)
        fit = fitness(self.list_portefeuille[0], 0) 
        self.list_portefeuille[0].score = fit.RatioSharpe()

        return self    
