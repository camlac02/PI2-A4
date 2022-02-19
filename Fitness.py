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
        
    def contrainte(portefeuille):
        connexion = Connexion('CAC40','root','Petruluigi0405@!')
        contrainte_limite = 0
        for i in portefeuille:
            contrainte_limite += i.rendements * i.nb_shares
        contrainte_limite = (contrainte_limite - 1)**2
        for i in portefeuille:
            requete = "Select rendements from CAC40 where noms ='"+ i.noms +"';"
            rendements_actif = connexion.execute(requete)
            for row in rendements_actif:
                contrainte_limite += max(0,row['rendements']-1)**2 +  max(0,row['rendements'])**2
        return contrainte_limite
    
    def heuristique(portefeuille):     ##Fonction à minimiser
        obj = -portefeuille.RatioSharpe() + 100*portefeuille.contrainte()
        return obj
