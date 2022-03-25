#Classe Fitness
class fitness():

    def __init__(self, portefeuille, sharpe):
        self.portefeuille = portefeuille
        self.sharpe = sharpe
    


    #Calcul du ratio de sharpe
    def RatioSharpe(self):
        ratio = (self.portefeuille.rendement)/(self.portefeuille.volatilite)
        self.sharpe = ratio
        return ratio
