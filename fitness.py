import Portefeuille
import Actifs

class fitness():
     def __init__(self, liste_Actifs, sharpe):
            self.liste_Actifs = liste_Actifs
            self.sharpe=sharpe
    
    #il faut récupérer la vol et le rendement attendu et le Sharpe attendu
    #attribuer des pénalités au score en fonction de l'ecart avec les données attendues
    