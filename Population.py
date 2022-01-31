from Portefeuille import Portefeuille 
from Actifs import Actifs
from Connexion import Connexion
class Population() :

    def __init__(self, list_portefeuille):
        self.list_portefeuille = list_portefeuille
    
    '''
    def Creation_Population(self, nb_portefeuille, MaxInvesti,connection,date):
        
        list_portefeuille = []
        for i in range(nb_portefeuille):
            #Creation de la liste d'actif
            list_asset = Portefeuille.Creation_list_actif(connection, date)
            #Creation du portefeuille
            p = Portefeuille(list_asset,0,0).Creation_Portefeuille(MaxInvesti)
            list_portefeuille.append(p)
            
            print('Creation portefeuille : '+str(i))
        #Ajout de la liste de portefeuille dans la population
        self.list_portefeuille = list_portefeuille
        return self
    
    '''
    def Creation_Population(self, list_asset, MaxInvest, nb_portefeuille):
        
        list_portefeuille = []

        for i in range(nb_portefeuille):
            

            p = Portefeuille(list_asset,0,0).Creation_Portefeuille(MaxInvest)
            list_portefeuille.append(p)

        self.list_portefeuille = list_portefeuille
        
        return self
    
    #Calcul des rendements moyens entre 2 dates

    def MoyenneRendements(self,Connexion,date1,date2):
        Liste=[]
        requete1="Select distinct name from helo;"
        curseur=Connexion.execute(requete1)
        ListeNoms=[]
        #on récupère la liste des noms des actifs
        for row in curseur:
            ListeNoms.append(row['name'])
        for name in ListeNoms:
            somme=0
            requete2="select Rendements from helo where name='"+name+"' and date between '"+date1+"' and '"+date2+"';"
            #on récupère la liste des Rendements de chaque actif
            curseur2=Connexion.execute(requete2)    
            nbrow=0
            for row in curseur2:
                somme+=(row['Rendements'])
                nbrow+=1
            moyenne=somme/nbrow
            Liste.append(moyenne)
        print(Liste)

    def __repr__(self):
        return "{0}".format(self.list_portefeuille)

if __name__=="__main__":
    pop = Population ([])
    connection = Connexion('cac','root','Jhanamal0004@')
    connection.initialisation()
    pop.MoyenneRendements(connection,"2017-11-09","2017-11-17")
    connection.close_connection()
