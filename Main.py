from datetime import date
from Connexion import Connexion
from Actifs import Actifs
from Population import Population
from Portefeuille import Portefeuille
from Fitness import Fitness

if __name__=="__main__":
    
    #Connexion a la base de donnée
    connection = Connexion('pi2','root','root')
    connection.initialisation()

    #Date de création du portefeuille
    date_test = "2016-07-01"

    #Date de fin
    date_actuelle = "2021-11-08"

    #Valeur Max de l'investissement
    max_invest = 5000
    
    #Nombre de portefeuilles par population
    nb_portefeuils = 4

    
    list_asset_with_value = []

    list_asset = Actifs.creationActifs(connection)

    #Associe une valeur a chaque actif
    for asset in list_asset:
            list_asset_with_value.append(asset.Valeur_Actifs(date_test,connection))
 
    #Creation de la population
    pop = Population([]) 

    pop.Creation_Population(list_asset_with_value, max_invest,nb_portefeuils)#connection,date_test)
    #pop.Creation_Population(nb_portefeuils, max_invest,connection,date_test)
    
    print(pop.__repr__())
    #PF = Portefeuille(list_asset, 0, 0)
    #PF.Creation_Portefeuille(max_invest)
    #print(PF)
    
    connection.close_connection()