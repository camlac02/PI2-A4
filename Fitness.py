from Actifs import Actifs
from Portefeuille import Portefeuille
import re
from math import sqrt
from Connexion import Connexion
from datetime import datetime

class Fitness():
    
    def __init__(self, portfeuille, debut):
        self.portfeuille=portfeuille
        self.debut=debut

    #Calcul du score du portefeuille suivant la volatilité et le rendement désiré
    def score(portefeuille, volatilite, rendement, debut, date):
        vol=0
        #Calcul de volatilité
        v=Fitness.Volatilite(portefeuille, debut, date)
        #Calcul de la somme de la différence de la volatilité voulue comparée à la volatilité du portefeuille
        vol = (v-volatilite)*(v-volatilite)
        print("La volatitilité du portfeuille est :",v,"%")
        
        #Calcul de rendement 
        r=Fitness.rendement(Fitness.tab_value_portfolio(portefeuille,debut,date))
        #Calcul de la somme de la différence du rendement voulu comparé au rendement du portefeuille
        rend = (r-rendement)*(r-rendement)
        print("Le rendement du portfeuille est :",r,"%")
        
        #Calcul du score comme la somme des différences
        score = vol + rend
        return score

    #
    def TabActifs(nom, debut, date):
        tableau=[]
        debut = date_to_int(debut)
        date = date_to_int(date)
        #Requête pour récupérer tous les actifs entre la date de début et la date de test
        requete = "SELECT * FROM cac where Date>="+str(debut)+" and Date<"+str(date)+";"
        conn = Connexion.execute(requete)
        curseur = conn.connection()
        for ligne in curseur:
            if (ligne[nom]!= 'PX_LAST'):
                #re.sub permet de remplacer les premiers éléments par le second
                NbShares = re.sub('\,+', '.', ligne[nom])
                #On ajoute le nombre de shares de chaque actif dans le tableau 
                #1 si la valeur n'est pas encore définie et le nombre de shares sinon
                if (NbShares=='#N/A N/A'):
                    tableau.append(1)
                else :
                    tableau.append(float(NbShares))
        conn.close_connection(curseur)
        return tableau

# Calcul de Volatilite
    def Volatilite(portfeuille, debut, date):
        taille=len(portfeuille.liste.Actifs)
        tab=[]
        #Calcul de variation pour chaque actif
        for i in range(0,taille):
            name1 = portfeuille.liste.Actifs[i].name
            a=Fitness.variation(Fitness.TabActifs(name1,debut, date))
            somme=0
            for j in range (0,taille):
                name2 = portfeuille.list_assets[j].name
                b=Fitness.variation(Fitness.TabActifs(name2,debut, date))
                value = portfeuille.list_assets[i].percentage * portfeuille.list_assets[j].percentage * Covariance(a,b)
                somme = somme + value
            tab.append(somme)
        var_potrfolio=0
        for t in range (0,len(tab)):
            var_potrfolio=var_potrfolio+tab[t]
        vol = sqrt(var_potrfolio)*100*sqrt(252)
        return vol

# Calcul de Variation
    def variation(tableau):
        tab_var=[]
        size = len(tableau)
        #(VF-VI)/VI
        for i in range(1,size):
            a=(tableau[i-1]/tableau[i]-1)
            tab_var.append(a)
        return tab_var


#Fonctions pour calcul du Fitness

#La moyenne est la somme des valeurs divisée par la quantité de valeurs
def Moyenne(tableau):
    total=0
    for i in range(0,len(tableau)):
        total = total+tableau[i]
    moyenne = total/len(tableau)
    return moyenne

#Idem pour la moyenne du score
def MoyenneScore(population):
    taille=len(population.list_portefeuille)
    total=0
    for i in range(0,taille):
        total += population.list_portfolio[i].score
    moyenne = total/taille
    return moyenne

#Calcul de covariance entre 2 tableaux 
def Covariance(a,b):
    #Vérification que les 2 tableaux ont la même taille
    if len(a) != len(b): 
        return 0 
    somme = 0 
    #Somme des (a(i)-Moyenne(a))(b(i)-Moyenne(b)) divisée par la longueur du tableau
    for i in range(0, len(a)): 
        somme = somme+ ((a[i] - Moyenne(a)) * (b[i] - Moyenne(b))) 
    resultat = somme/(len(a))
    return resultat

#Tri du tableau
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

#Conversion d'un entier en date
def int_to_date(nb):
    date=datetime.fromtimestamp(nb).strftime("%Y-%m-%d")
    return date

#Conversion inverse de date en entier
def date_to_int(date): #format en str : 01/01/2010
    date=datetime.strptime(date,"%d/%m/%Y")
    nb = int(date.strftime('%s'))+7200
    return nb