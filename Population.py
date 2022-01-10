from Portefeuille import Portefeuille 
from Actifs import Actifs

class Population() :

    def __init__(self, list_portefeuille):
        self.list_portefeuille = list_portefeuille
    
    def Creation_Population(self, nb_portefeuille, MaxInvesti,connection,date):
        
        list_portefeuille = []

        for i in range(nb_portefeuille):

            #Creation de la liste d'actif
            list_asset = Portefeuille.Creation_list_actif(connection, date)

            #Creation du portefeuille
            p = Portefeuille(list_asset,0,0).Creation_Portefeuille(MaxInvesti)
            list_portefeuille.append(p)
            
            print('Creation portefeuille : '+str(i))

        #Ajout de la liste de portefeuille dans la population
        self.list_portefeuille = list_portefeuille

        return self
    
    '''
    def Creation_Population(self, list_asset, MaxInvest, nb_portefeuille):
        
        list_portefeuille = []

        for i in range(nb_portefeuille):
            p = Portefeuille(list_asset,0,0).Creation_Portefeuille(MaxInvest)
            list_portefeuille.append(p)

        for i in list_portefeuille:
            print(i)

        self.list_portefeuille = list_portefeuille
        
        return self
    '''

    def __repr__(self):
        return "{0}".format(self.list_portefeuille)



