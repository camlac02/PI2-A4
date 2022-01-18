import pymysql.cursors

class Connexion():

    def __init__(self, database, user, mdp):
        self.database = database
        self.user = user
        self.mdp = mdp
        self.conn = None
        self.cur = None


    def initialisation(self):
        #La fonction ouvre la connexion avec la base de donnée
        self.conn = pymysql.connect(host='localhost',
                            user=self.user,
                            password=self.mdp,
                            db=self.database,
                            cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()


    def execute(self,requete):
        #La fonction prend en argument une requete SQL sous forme de chaine de caractère
        #Et retourne le curseur qui permet d'acceder au résultat de la requete     
        self.cur.execute(requete)
        return self.cur


    def close_connection(self):    
        #La fonction ferme la connexion avec la Base de donnés
        self.cur.close()
        self.conn.close()