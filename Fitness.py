# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:00:06 2022

@author: PC
"""

from Connexion import Connexion
import Portefeuille
import Actifs

class fitness():
    def __init__(self, portefeuille, sharpe):
        self.portefeuille = portefeuille
        self.sharpe = sharpe
    
    def RatioSharpe(self):
        ratio = (self.portefeuille.rendement)/(self.portefeuille.volatilite)
        self.sharpe = ratio
        return ratio
