#Classe Fitness
class fitness():

    def __init__(self, portefeuille):
        self.portefeuille = portefeuille
        self.sharpe = 0

    #Calcul du ratio de sharpe
    def RatioSharpe(self):
        ratio = (self.portefeuille.rendement)/(self.portefeuille.volatilite)
        self.sharpe = ratio
        return ratio