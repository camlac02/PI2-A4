from math import nan
from Connexion import Connexion
from Actifs import Actifs
#from Population import Population
from Portefeuille import Portefeuille
from Population import Population
from pandas import DataFrame
import pandas
import csv
if __name__=="__main__":
    
    #Connexion a la base de donnée
    connection = Connexion('cac','root','Jhanamal0004@')
    connection.initialisation()

    #Date de création du portefeuille
    date_test = "01/07/2016"

    #Valeur Max de l'investissement
    max_invest = 5000
    
    #Nombre de portefeuilles par population
    nb_portefeuils = 4

    
    list_asset_with_value = []
    

    list_asset = Actifs.creationActifs(connection)

    #Associe une valeur a chaque actif
    for asset in list_asset:
            list_asset_with_value.append(asset.Valeur_Actifs(date_test,connection))

    #print(list_asset_with_value)
    #Creation de la population
    pop = Population([]) 

    print('creation des portefeuilles')

    pop.Creation_Population(list_asset_with_value, max_invest,nb_portefeuils)#connection,date_test)
    #pop.Creation_Population(nb_portefeuils, max_invest,connection,date_test)

    print(pop.__repr__())

    
    connection.close_connection()