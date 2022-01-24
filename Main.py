
from Connexion import Connexion
from Actifs import Actifs
from Population import Population
from Portefeuille import Portefeuille

if __name__=="__main__":
        
    #Connexion a la base de donnée
    connection = Connexion('pi2','root','Leo20-Esilv')
    connection.initialisation()

    #Date de création du portefeuille
    date_test = "2016-07-01"

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

    
    connection.close_connection()


