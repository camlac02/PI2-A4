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

    #Tableau des nombres de Shares 
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
    def Volatilite(portefeuille, debut, date):
        taille=len(portefeuille.liste.Actifs)
        tab=[]
        #Calcul de variation pour chaque actif
        for i in range(0,taille):
            nom1 = portefeuille.liste_Actifs[i].nom
            a=Fitness.variation(Fitness.TabActifs(nom1,debut, date))
            somme=0
            #Somme des covariances pondérées par les volumes
            for j in range (0,taille):
                nom2 = portefeuille.liste_Actifs[j].nom
                b=Fitness.variation(Fitness.TabActifs(nom2,debut, date))
                somme = somme + portefeuille.liste_Actifs[i].volume * portefeuille.liste_Actifs[j].volume* Covariance(a,b)
            tab.append(somme)
        varPF=0
        for t in range (0,len(tab)):
            varPF=varPF+tab[t]
        vol = sqrt(varPF)*100*sqrt(252)
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

#Calcul de rendement
    def rendement(tableau):
        i=0
        res=1
        tabRendements=[]
        #Création d'un tableau des rendements
        while i<len(tableau)-1:
            tabRendements.append((tableau[i+1]-tableau[i])/(tableau[i]))
            i=i+1
        j=0
        #Produit des rendements (1+r) 
        while j<len(tabRendements):
            res=res*(1+tabRendements[j])
            j=j+1
        #Pourcentage de rendements
        return (res-1)*100

#Calcul des valeurs de portefeuilles
    def tabValPF(portefeuille,debut, date):
        tabVal=[]
        tab_Noms=Actifs.creationActifs()
        tabValPf=[]
        i=0
        #Tableau avec le nombre de shares selon le nombre d'actifs
        while i<len(tab_Noms):
            tabVal.append(Fitness.TabActifs(tab_Noms[i].nom,debut, date))
            i=i+1
        t=0
        #Somme des valeurs de chaque actif du portefeuille (contenu dans le tableau de valeurs) multiplié par le nombre de shares 
        while t<len(tabVal[0]):
            j=0
            total=0
            while j<len(tabVal):
                total=total+portefeuille.liste_Actifs[j].nb_shares*tabVal[j][t]
                j=j+1
            tabValPf.append(total)
            t=t+1
        return tabValPf

#Fonctions pour aider à calculer le Fitness

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