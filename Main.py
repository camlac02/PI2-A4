
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
    nb_portefeuils = 2

    #Creation de la population
    pop = Population([]) 

    pop.Creation_Population(nb_portefeuils, max_invest,connection,date_test)

    print(pop.__repr__())


    connection.close_connection()


