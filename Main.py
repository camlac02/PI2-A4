from Actif import Actif
from Connexion import Connexion

if __name__=="__main__":
    
    connection = Connexion('pi2','root','Leo20-Esilv')
    connection.initialisation()

    date_test="2016-07-01"
    list_asset = Actif.creationActif(connection)
    list_asset_with_value = Actif.Valeur_Actif(list_asset,date_test,connection)
    
    for Asset in list_asset_with_value:
        print(Asset.__repr__()) 

    connection.close_connection()
