
from AlgoG import AlgoG
from Connexion import Connexion
from Actifs import Actifs
from Population import Population
from Portefeuille import Portefeuille

if __name__=="__main__":
        
    #Connexion a la base de donnée
    connection = Connexion('pi2','root','Leo20-Esilv')
    connection.initialisation()

    #Date de création du portefeuille
    date_1 = "2017-01-05"
    date_2 = "2017-12-29"



    #Valeur Max de l'investissement
    max_invest = 300000

    #Nombre de portefeuilles par population
    nb_portefeuils = 5
    
    list_asset_with_value = []

    list_asset = Actifs.creationActifs(connection)

    #Associe une valeur a chaque actif
    for asset in list_asset:
            list_asset_with_value.append(asset.Valeur_Actifs(date_1,date_2,connection))
            #list_asset_with_value.append(asset.Valeur_Actifs(date_1,connection))
 
    #Creation de la population
    pop = Population([]) 

    pop.creation_population( list_asset_with_value, max_invest,nb_portefeuils)#connection,date_test)
    
    print(pop.__repr__())
    
    Generation_max = 5

    algoG = AlgoG(pop,Generation_max).algorihtme_genetique(list_asset_with_value, max_invest)

    print('\nPortefeuille final :\n'+algoG.__repr__())

    connection.close_connection()
