from Actifs import Actifs
from Portefeuille import Portefeuille
import re
from math import sqrt
from Connexion import Connexion
from datetime import datetime

#test

class Fitness():
    
    def __init__(self, portfeuille, debut):
        self.portfeuille=portfeuille
        self.debut=debut

    def score(portefeuille, volatilite, rendement, debut, date):
        v=Fitness.Volatilite(portefeuille, debut, date)
        return score

    def Volatilite(portfeuille, debut, date):
        taille=len(portfeuille.liste.Actifs)
        tab=[]
        for i in range(0,taille):
            name1 = portfeuille.liste.Actifs[i].name
            a=Fitness.variation_actif(Fitness.tab_actif(name1,debut, date))
            summ=0
            for j in range (0,taille):
                name2 = portfeuille.list_assets[j].name
                b=Fitness.variation_actif(Fitness.tab_actif(name2,debut, date))
                value = portfeuille.list_assets[i].percentage * portfeuille.list_assets[j].percentage * Covariance(a,b)
                summ = summ + value
            tab.append(summ)
        var_potrfolio=0
        for t in range (0,len(tab)):
            var_potrfolio=var_potrfolio+tab[t]
        vol = sqrt(var_potrfolio)*100*sqrt(252)
        return vol

    def variation_actif(tab_actif):
        tab_var=[]
        size = len(tab_actif)
        for i in range(1,size):
            a=(tab_actif[i-1]/tab_actif[i]-1)
            tab_var.append(a)
        return tab_var


#Fonctions pour calcul du Fitness

def Moyenne(tableau):
    total=0
    for i in range(0,len(tableau)):
        total = total+tableau[i]
    moyenne = total/len(tableau)
    return moyenne

def MoyenneScore(population):
    taille=len(population.list_portefeuille)
    total=0
    for i in range(0,taille):
        total += population.list_portfolio[i].score
    moyenne = total/taille
    return moyenne

def Covariance(a,b):
    if len(a) != len(b): 
        return 0
    Ma = Moyenne(a) 
    Mb = Moyenne(b) 
    somme = 0 
    for i in range(0, len(a)): 
        somme = somme+ ((a[i] - Ma) * (b[i] - Mb)) 
    resultat = somme/(len(a))
    return resultat

def Carre(a):
    return a*a


def Tri(tableau):
    for i in range(1,len(tableau)):
        element = tableau[i]
        j = i
        #Décalage des éléments du tableau
        while j>0 and tableau[j-1]>element:
            tableau[j]=tableau[j-1]
            j = j-1
        #Insertion l'élément à sa place
        tableau[j]=element
    return tableau         

def int_to_date(nb):
    date=datetime.fromtimestamp(nb).strftime("%Y-%m-%d")
    return date

def date_to_int(date): #format en str : 01/01/2010
    date=datetime.strptime(date,"%d/%m/%Y")
    nb = int(date.strftime('%s'))+7200
    return nb