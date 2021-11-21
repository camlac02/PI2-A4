#Classe Connexion
import pymysql.cursors

#Connexion avec la base de données
class Connexion():
   
    def __init__(self, bdd, utilisateur, MotDePasse):
        self.bdd = bdd
        self.utilisateur = utilisateur
        self.MotDePasse = MotDePasse
        self.conn = None
        self.cur = None

    def initialisation(self):
        #Fonction qui prend en argument la connexion
        #La fonction ouvre la connexion avec la base de données
        self.conn = pymysql.connect(host='localhost',
                            utilisateur=self.utilisateur,
                            MDP=self.MotDePasse,
                            bdd=self.bdd,
                            cursorclasse=pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()

    def execute(self,requete):
        #Fonction qui prend en argument la connexion et une requête comme chaîne de caractère
        #qui correspond à une requête de base de données
        #La fonction retourne le curseur pour accéder au résultat de la requête
        self.cur.execute(requete)
        return self.cur

    def close_connection(self):
        #Fonction qui prend en argument la connexion et ferme cette connexion
        self.cur.close()
        self.conn.close()