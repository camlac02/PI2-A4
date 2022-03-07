class fitness():

    def __init__(self, portefeuille, sharpe):
        self.portefeuille = portefeuille
        self.sharpe = sharpe

    def RatioSharpe(self):
        ratio = (self.portefeuille.rendement)/(self.portefeuille.volatilite)
        return ratio