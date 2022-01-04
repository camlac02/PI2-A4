
from Connexion import Connexion
from Actifs import Actifs
from Population import Population
from Portefeuille import Portefeuille

if __name__=="__main__":
    
    connection = Connexion('pi2','root','Leo20-Esilv')
    connection.initialisation()

    # Creation des Actifs (seulement avec le nom)
    list_asset = Actifs.creationActifs(connection)

    date_test = "2016-07-01"
    list_asset_with_value = []

    # Associe une valeur a chaque actif pour une date donnée
    for asset in list_asset:
        list_asset_with_value.append(asset.Valeur_Actifs(date_test,connection))  

    # Creation du portefeuille
        #Valeur Max de l'investissement
    max_invest = 10000
    portefeuil_1 = Portefeuille(list_asset_with_value,0)
    portefeuil_1.Creation_Portefeuille(max_invest)

    #print(portefeuil_1.__repr__())

    liste_portefeuil = [0,0,0]

    pop = Population(liste_portefeuil) 

    pop.Creation_Population(3,max_invest,list_asset_with_value)
    print(pop.__repr__())

    connection.close_connection()


