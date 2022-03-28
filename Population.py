from copy import deepcopy
from Portefeuille import Portefeuille 
from Fitness import fitness

#Classe Population
class Population() :

    def __init__(self, list_portefeuille):
        self.list_portefeuille = list_portefeuille

    def creation_population(self, list_asset, MaxInvest, nb_portefeuille,date_1,date_2,connexion):
    #Creation de la population en fonction du nombre de portefeuille voulu.
        list_portefeuille = []
        for i in range(nb_portefeuille):
            #Creation de chaque portefeuille de la population
            p = Portefeuille(list_asset,0,0,0,0).Creation_Portefeuille(MaxInvest,date_1,date_2,connexion)
            list_portefeuille.append(p) #On ajoute le portefeuille à la liste de portefeuille qui va composer la population

        self.list_portefeuille = list_portefeuille
        return self

    #Retourne une chaine de caractère contenant la liste de portefeuilles contenu dans une population.
    def __repr__(self):
        return "{0}".format(self.list_portefeuille)

    #Fonction prenant en paramètre deux portefeuilles. Les listes d'actifs de ces deux portefeuilles
    #Sont coupées en deux et recombiné afin de crée deux nouvelles listes d'actifs.
    #Deux nouveaux portefeuilles sont générés à partir de ces deux nouvelles listes
    def crossover(portefeuille_1, portefeuille_2,date_1,date_2,connexion):
        
        list_1 = deepcopy(portefeuille_1.liste_Actifs)
        list_2 = deepcopy(portefeuille_2.liste_Actifs)

        #On crée une liste 'shares_1' composé des actions de la liste_1
        #dont le nombre de share est non nul
        shares_1 = []
        for i in range(len(list_1)):
            if(list_1[i].nb_shares != 0):
                shares_1.append(list_1[i])

        #On garde la moitié de ces actions
        shares_1 = shares_1[0:len(shares_1)//2]

        #On calcule la valeur de la liste shares_1 
        value_1 = 0
        for actif in shares_1:
            value_1 += actif.nb_shares*actif.valeur
        print('Valeur du croisement sur liste 1: '+str(value_1))
        
        #On crée une liste 'shares_2' composé des actions de la liste_2
        #dont le nombre de share est non nul
        shares_2 = []
        for i in range(len(list_2)):
            if(list_2[i].nb_shares != 0):
                shares_2.append(list_2[i])

        #On inverse la liste
        shares_2 = shares_2[::-1]

        #On crée une nouvelle liste composé des actions de shares_2. 
        #Ces actions sont ajouté jusqu'à ce que la valeur de la nouvelle liste
        #atteigne la valeur de shares_1 afin que ces deux listes aient la meme valeur
        mut2 = []
        value_2 = 0
        for j in range(len(shares_2)):
            nb = 0
            while ((shares_2[j].valeur * nb) < value_1) and nb <= shares_2[j].nb_shares:
                nb += 1
            actif = deepcopy(shares_2[j])
            actif.nb_shares = nb-1
            value_1 -= actif.valeur * actif.nb_shares
            value_2 += actif.nb_shares * actif.valeur
            mut2.append(actif)

        print('\nValeur du croisement sur liste 2',value_2,'\n')

        #mut1 est une deepcopy de shares_1 pour éviter les problèmes de doublons
        mut1 = deepcopy(shares_1)

        #On retire les actions de la liste mut1 à liste_1
        for i in range(len(list_1)):
            for j in range(len(shares_1)):
                if list_1[i].nom == shares_1[j].nom:
                    list_1[i].nb_shares -= shares_1[j].nb_shares

        #On retire les actions de la liste mut2 à liste_2
        for i in range(len(list_2)):
            for j in range(len(mut2)):
                if list_2[i].nom == mut2[j].nom:
                    list_2[i].nb_shares -= mut2[j].nb_shares

        #On ajoute les actions de la liste mut2 à la liste_1
        for i in range(len(list_1)):
            for j in range(len(mut2)):
                if list_1[i].nom == mut2[j].nom:
                    list_1[i].nb_shares += mut2[j].nb_shares
        
        #On ajoute les actions de la liste mut1 à la liste_2
        for i in range(len(list_2)):
            for j in range(len(mut1)):
                if list_2[i].nom == mut1[j].nom:
                    list_2[i].nb_shares += mut1[j].nb_shares        
    
        #On crée des portefeuilles composés des deux nouvelles listes crées
        final_mut1 = Portefeuille(list_1,0,0,0,0)
        final_mut2 = Portefeuille(list_2,0,0,0,0)

        #On associe des valeurs à ces deux nouveaux portefeuilles

        final_mut1.Valeur_Portefeuille()
        final_mut1.Poid_dans_portefeuille()
        final_mut1.VolPortefeuille(date_1,date_2,connexion)
        final_mut1.RendementsPF()
        #On calcul le score du portefeuille grace a la fitness
        final_mut1.score = fitness(final_mut1).RatioSharpe()

        final_mut2.Valeur_Portefeuille()
        final_mut2.Poid_dans_portefeuille()
        final_mut2.VolPortefeuille(date_1,date_2,connexion)
        final_mut2.RendementsPF()
        #On calcul le score du portefeuille grace a la fitness
        final_mut2.score = fitness(final_mut2).RatioSharpe()

        #On retourne les deux nouveaux portefeuilles crées
        return [final_mut1,final_mut2]