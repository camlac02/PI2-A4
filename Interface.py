#Données rentrées par l'utilisateur
from tkinter import *

fenetre=Tk()
fenetre.title("Données")

RiskLabel = Label(fenetre, text = "Quel est le risque maximal souhaité")
RiskLabel.pack()

risk = StringVar()
saisie = Entry(fenetre, textvariable = risk, width = 10)
saisie.pack()

InvestLabel = Label(fenetre, text = "Quel est l'investissement maximal souhaité")
InvestLabel.pack()

invest = StringVar()
saisie2 = Entry(fenetre, textvariable = invest, width = 10)
saisie2.pack()

bouton1 = Button(fenetre, text = "CALCULER", width=8)
bouton1.pack()

Resultat = Label(fenetre, text="Le meilleur portefeuille est :")
Resultat.pack()

fenetre.mainloop()


#Graphiques
from matplotlib import pyplot as plt
from Actifs import Actifs
from Connexion import Connexion
#Connexion a la base de donnée
connection = Connexion('pi2','root','root')
connection.initialisation()
list_assets = Actifs.creationActifs(connection)
rendements = []
volatilites = []
for i in range(len(list_assets)):
    rendements.append(list_assets[i].rendement)

plt.plot(list_assets, rendements)
plt.title("Graphique actifs")
plt.xlabel("Volatilités actifs")
plt.ylabel("Rendements actifs")
plt.show()