# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:00:06 2022

@author: PC
"""

from Connexion import Connexion
import Portefeuille
import Actifs

class fitness():
    def __init__(self, liste_Actifs, sharpe):
        self.liste_Actifs = liste_Actifs
        self.sharpe=sharpe
    
    def heuristique(portefeuille):     ##Fonction à minimiser
        obj = -portefeuille.RatioSharpe() + 100*portefeuille.Contrainte()
        return obj
