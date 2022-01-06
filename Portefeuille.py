#Classe Portefeuille
from Actifs import Actifs
import  random

class Portefeuille():

    def __init__(self, liste_Actifs, valeur, score):
        self.liste_Actifs = liste_Actifs
        self.valeur = valeur
        self.score = score

    #Créé un portefeuil composé d'une liste d'action aléatoire
    def Creation_Portefeuille(self, MaxInvesti):
        print('TOUR')
        prix_min = self.plus_petit_prix() 
        assets = list(range(len(self.liste_Actifs))) # liste des index de tous les actifs du portefeuille   
        
        for i in range(len(self.liste_Actifs)):
            self.liste_Actifs[i].nb_shares = 0
            print(str(self.liste_Actifs[i].nb_shares)+'\n')

        while (MaxInvesti > prix_min and len(assets) !=0 ):
        # Tant que la valeur a investir (MaxInvest) est superieur au prix de l'actif le moins cher
        # Et tant que la liste des index des actifs du portefeuil n'est pas vide
        # on ajoute une action au portefeuille

            # Selection aléatoire d'une action via son index dans la liste d'actif
            choice_asset = int(random.choice(assets))
            assets.remove(choice_asset) # On retire l'index de la liste pour ne pas tomber deux fois sur le même actif
            # Nombre maximal de shares que l'on peut acheter pour cet actif
            max_nb = MaxInvesti//(self.liste_Actifs[choice_asset].valeur)
            # Selection du nombre de shares entre 0 et nb_max 
            

            #self.liste_nbr_shares[choice_asset] = random.randint(0,max_nb)
            self.liste_Actifs[choice_asset].nb_shares = random.randint(0,max_nb)
            # On reduit la valeur a investir en lui retirant la valeur des parts de l'actif choisi
            MaxInvesti = MaxInvesti - self.liste_Actifs[choice_asset].nb_shares*self.liste_Actifs[choice_asset].valeur
            #MaxInvesti = MaxInvesti - int(self.liste_nbr_shares[choice_asset])*self.liste_Actifs[choice_asset].valeur

        self.Valeur_Portefeuille()
        #self.Poid_dans_portefeuille()
        return self


    # Calcul la valeur d'un portefeuille
    def Valeur_Portefeuille(self):
        #Fonction qui prend en argument un portefeuille et qui calcule
        #la valeur associée à ce portefeuille 
        self.liste_Actifs
        for i in range(len( self.liste_Actifs)):
            #valeur=valeur asset*poids
            self.valeur = self.valeur +  self.liste_Actifs[i].valeur*int( self.liste_Actifs[i].nb_shares)
            #self.valeur = self.valeur +  self.liste_Actifs[i].valeur*int( self.liste_nbr_shares [i])
        return self


    # Calcul le prix de l'actif avec le plus faible 
    def plus_petit_prix(self):
        min = self.liste_Actifs[0].valeur
        for asset in self.liste_Actifs:
            if asset.valeur < min:
                min = asset.valeur
        return min 

    #################################################################################################################################
    #Defini le poid qu'a l'action dans le portefeuille
    def Poid_dans_portefeuille(self):
        for i in range(len(self.liste_Actifs)):
            poids = self.liste_Actifs[i].valeur * self.liste_Actifs[i].nb_shares
            self.liste_Actifs[i].poids  = round(poids / self.Valeur_Portefeuille()*100,2)
        return self
    ####################################################################################################################################
    
    
    def __repr__(self):
        return "{0}\nValeur du portefeuil : {2}\nScore du portefeuille : {1}\n\n".format(self.liste_Actifs,self.score,self.valeur) 
           
    '''
    def __repr__(self):    
        for i in range(len(self.liste_nbr_shares)):
            print("{0}, Nbr of shares : {1}".format(self.liste_Actifs[i],self.liste_nbr_shares[i]) )
        print("\nValeur du portefeuil : {0}\nScore du portefeuille : {1}\n\n".format(self.valeur,self.score))
    '''