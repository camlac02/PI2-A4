# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:57:23 2022

@author: PC
"""
from AlgoG import AlgoG
from Connexion import Connexion
from Actifs import Actifs
from Population import Population
from Portefeuille import Portefeuille

if __name__=="__main__":

    #Connexion a la base de donnée
    connection = Connexion('BDD','root','PetruLuigi0405@!')
    connection.initialisation()

    #Date de création du portefeuille
    date_1 = "2017-01-05"
    date_2 = "2017-12-29"

    #Valeur Max de l'investissement
    max_invest = 300000
    
    # Saisie utilisateur
    expected_return = float(input("Quel rendement souhaitez vous atteindre ? :"))
    expected_std = float(input("Quel volatilité souhaitez vous atteindre ? :"))
    
    #Nombre de portefeuilles par population
    nb_portefeuils = 4

    list_asset_with_value = []

    list_asset = Actifs.creationActifs(connection)

    #Associe une valeur a chaque actif
    for asset in list_asset:
            list_asset_with_value.append(asset.Valeur_Actifs(date_1,date_2,connection))
            #list_asset_with_value.append(asset.Valeur_Actifs(date_1,connection))

    pop = Population([]) 

    pop.creation_population( list_asset_with_value, max_invest,nb_portefeuils)

    print(pop.__repr__())


    Generation_max = 10
    
        #Appel de l'algo G
    algoG = AlgoG(pop,Generation_max).algorihtme_genetique(list_asset_with_value, max_invest,expected_return, expected_std)

    print('\nPortefeuille final :\n'+algoG.__repr__())

    connection.close_connection()
