#from multiprocessing import Value
from unicodedata import name
from Portefeuille import Portefeuille 
from Actifs import Actifs
import random
from Fitness import fitness
from copy import deepcopy

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


    def crossover(self, max_invest, i):
        
        print('debut crossover')
        liste_portefeuille = deepcopy(self.list_portefeuille)

        parent1 = deepcopy(liste_portefeuille[i])
        parent1_actifs =  deepcopy(parent1.liste_Actifs)

        parent2 = deepcopy(liste_portefeuille[i+1])
        parent2_actifs = deepcopy(parent2.liste_Actifs)

        #On crée une liste avec tous les actifs de parent 1 ayant un nombre de shares > 0
        list = []
        for actif in parent1_actifs:
            if actif.nb_shares != 0:
                list.append(actif)
        
        #On selectionne la moitié de ces actifs et on les ajoute à une liste_1
        #qui sera la liste des actifs qui seront ajouté à parent 2 
        #val étant la valeur de ces actifs 
        val = 0
        list_1 = []
        for i in range(len(list)//3):
            val += list[-i].nb_shares * list[-i].valeur 
            list_1.append(list[-i])


        #On crée la liste des actifs de parents 2 qui seront ajoutés à parent 1
        list_2 = []
        val_2 = 0
        for actif in parent2_actifs :
            if actif.nb_shares != 0:
                if ((val_2 + actif.nb_shares * actif.valeur) < val):
                    val_2 += actif.nb_shares * actif.valeur
                    list_2.append(actif)
                elif (val_2 < val):
                    nb=0
                    while nb < actif.nb_shares and val_2 < val:
                        val_2 += actif.valeur
                        nb+=1
                    if nb != 0:
                        actif.nb_shares = nb
                    list_2.append(actif)

        #On print la valeur des deux listes
        #print('val ',val) 
        #print('val_2 ',val_2) 

        #On affiche les deux listes
        #print('list 1 : \n',list_1)
        #print('list 2 : \n',list_2)

        #On ajoute les actifs de la liste 2 à parent 1
        for i in range(len(parent1_actifs)):
            for actif in list_2:
                if actif.nom == parent1_actifs[i].nom:
                    #print('Ajouté à parent 1 '+actif.nom, '  ', actif.nb_shares )
                    parent1_actifs[i].nb_shares += deepcopy(actif.nb_shares)

        l_1 = deepcopy(list_1)

        #On remet à 0 le nombre de share des actifs selectionnés dans list_1 dans parent 1
        for i in range(len(parent1_actifs)):
            for actif in deepcopy(list_1):
                if actif.nom == parent1_actifs[i].nom:
                    parent1_actifs[i].nb_shares = 0

        for i in range(len(parent2_actifs)):
            for actif in deepcopy(list_2):
                if actif.nom == parent2_actifs [i].nom:
                    parent2_actifs [i].nb_shares = 0       

        #print('parent 1 : \n',parent1_actifs)
        #print('parent 2 : \n',parent2_actifs )

        for i in range(len(parent2_actifs )):
            for actif in l_1:
                if actif.nom == parent2_actifs [i].nom:
                    #print('Ajouté à parent 2 '+actif.nom, '  ', actif.nb_shares )
                    parent2_actifs[i].nb_shares += deepcopy(actif.nb_shares) 

        #print('parent 1 : \n',parent1_actifs)
        #print('parent 2 : \n',parent2_actifs )

        mut1=Portefeuille(parent1_actifs,0,0,0,0)
        mut2=Portefeuille(parent2_actifs,0,0,0,0)

        #print(len(mut1.liste_Actifs))
        #print(len(mut2.liste_Actifs))

        liste_Actif = mut1.liste_Actifs
        mut1.Valeur_Portefeuille()
        print(mut1.valeur)
        mut1.Poid_dans_portefeuille() # calcule la valeur finale du portefeuille
        mut1.VolPortefeuille(liste_Actif)
        mut1.RendementsPF(liste_Actif)
        fit = fitness(mut1, 0) 
        mut1.score = fit.RatioSharpe()

        liste_Actif = mut2.liste_Actifs
        mut2.Valeur_Portefeuille()
        print(mut2.valeur)
        mut2.Poid_dans_portefeuille() # calcule la valeur finale du portefeuille
        mut2.VolPortefeuille(liste_Actif)
        mut2.RendementsPF(liste_Actif)
        fit = fitness(mut2, 0) 
        mut2.score = fit.RatioSharpe()

        print('Fin du crossover')

        return [mut1,mut2]   