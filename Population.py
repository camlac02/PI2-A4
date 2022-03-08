#from multiprocessing import Value
from unicodedata import name
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
        parent2= list_trie[2]
        mut1=Portefeuille([],0,0,0,0)
        mut2=Portefeuille([],0,0,0,0)
        while mut1.Valeur_Portefeuille().valeur < alpha: #Trouver une solution pour tomber exactement sur le max invest, ce faire une marge sur le pourcentage effectué pour ne pas dépasser ?
            mut1.liste_Actifs.append(parent1.liste_Actifs.pop())
        while mut2.Valeur_Portefeuille().valeur <alpha:
            mut2.liste_Actifs.append(parent2.liste_Actifs.pop())

        print(len(mut1.liste_Actifs))
        print(len(parent1.liste_Actifs))
        print(len(mut2.liste_Actifs))
        print(len(parent2.liste_Actifs))

        # new_parent1 = Portefeuille(parent1.liste_Actifs,0,0,0,0)
        # new_parent2 = Portefeuille(parent2.liste_Actifs,0,0,0,0)

        # for actif in mut2.liste_Actifs: 
        #     for actif_parent in new_parent1.liste_Actifs:
        #         if actif_parent.nom == actif.nom :
        #             actif_parent.nb_shares += actif.nb_shares
        #         else :
        #             new_parent1.liste_Actifs.append(actif) 
        
        # for actif in mut1.liste_Actifs: 
        #     for actif_parent in new_parent2.liste_Actifs:
        #         if actif_parent.nom == actif.nom :
        #             actif_parent.nb_shares += actif.nb_shares
        #         else :
        #             new_parent2.liste_Actifs.append(actif)     

        new_parent1 = Portefeuille(parent1.liste_Actifs + mut2.liste_Actifs,0,0,0,0)
        new_parent2 = Portefeuille(parent2.liste_Actifs + mut1.liste_Actifs,0,0,0,0)

        print(len(new_parent1.liste_Actifs))
        print(len(new_parent2.liste_Actifs))

        #remplacement des anciens portefeuilles par les nouveaux(ou seulement ajout des nouveaux si on le souhaite)
        list_trie.pop(2)
        list_trie.pop(1)
        list_trie.append(new_parent1)
        list_trie.append(new_parent2)
        self.list_portefeuille = list_trie
        self.__repr__()

 
        liste_Actif = self.list_portefeuille[-1].liste_Actifs
        self.list_portefeuille[-1].Valeur_Portefeuille()
        self.list_portefeuille[-1].Poid_dans_portefeuille() # calcule la valeur finale du portefeuille
        self.list_portefeuille[-1].VolPortefeuille(liste_Actif)
        self.list_portefeuille[-1].RendementsPF(liste_Actif)
        fit = fitness(self.list_portefeuille[-1], 0) 
        self.list_portefeuille[-1].score = fit.RatioSharpe()

        liste_Actif = self.list_portefeuille[-2].liste_Actifs
        self.list_portefeuille[-2].Valeur_Portefeuille()
        self.list_portefeuille[-2].Poid_dans_portefeuille() # calcule la valeur finale du portefeuille
        self.list_portefeuille[-2].VolPortefeuille(liste_Actif)
        self.list_portefeuille[-2].RendementsPF(liste_Actif)
        fit = fitness(self.list_portefeuille[-2], 0) 
        self.list_portefeuille[-2].score = fit.RatioSharpe()

        return self    
