
from Connexion import Connexion
from Actifs import Actifs

if __name__=="__main__":
    
    connection = Connexion('pi2','root','Leo20-Esilv')
    connection.initialisation()

    date_test="2016-07-01"
    
    list_asset = Actifs.creationActif(connection)
    list_asset_with_value = Actifs.Valeur_Actif(list_asset,date_test,connection)
    
    #print(Actif.Rendement_Actif('BNP',connection))
    
    for Asset in list_asset_with_value:
        print(Asset.__repr__()) 

    connection.close_connection()
