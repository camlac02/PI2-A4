from AlgoG import AlgoG
from Connexion import Connexion
from Actifs import Actifs
from Population import Population

if __name__=="__main__":

    #Connexion a la base de donnée
    connection = Connexion('pi2','root','Leo20-Esilv')
    connection.initialisation()

    #Date de création du portefeuille
    date_1 = "2017-01-05"
    date_2 = "2017-12-29"

    print("Si vous ne souhaitez pas renseigner de volatilité ou de rendement à atteindre entrez : 0")

    #Valeur Max de l'investissement
    max_invest = float(input("Quel est le montant que vous souhaitez investir ? : "))
    #max_invest = 300000
    
    #Valeur visée pour le rendement et la volatilitée
    expected_return = float(input("Quel rendement souhaitez vous atteindre ? : "))
    expected_std = float(input("Quelle volatilité souhaitez vous atteindre ? : "))
    
    #Nombre de portefeuilles par population
    nb_portefeuils = 5
    Generation_max = 5

    #Creation des différents actifs
    list_asset_with_value = []
    list_asset = Actifs.creationActifs(connection)

    #Associe une valeur a chaque actif
    for asset in list_asset:
            list_asset_with_value.append(asset.Valeur_Actifs(date_1,date_2,connection))


    #Creation de la population initiale
    pop = Population([])
    pop.creation_population(list_asset_with_value, max_invest,nb_portefeuils,date_1,date_2,connection)
    print(pop.__repr__())

    #Appel de l'algo Génétique
    algoG = AlgoG(pop,Generation_max).algorihtme_genetique(list_asset_with_value, max_invest,expected_return, expected_std,date_1,date_2,connection)

    print('\nPortefeuille final :\n'+algoG.__repr__())
    print('\n', algoG.liste_Actifs.__str__())

    connection.close_connection()
