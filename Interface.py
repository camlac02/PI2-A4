#Données rentrées par l'utilisateur
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from AlgoG import AlgoG
from Connexion import Connexion
from Actifs import Actifs
from Population import Population
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 


class Interface(tk.Tk):
    
    def __init__(self) :
        super().__init__()

        def getEntry():
            res = self.saisie.get()
            self.max_invest=float(res)
            res = self.saisie2.get()
            self.expected_return=float(res)
            res = self.saisie3.get()
            self.expected_std=float(res)
            
        def plot(): 
            fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
  
            y = [i**2 for i in range(101)] 
    
            plot1 = fig.add_subplot(111) 
            plot1.plot(y) 
  
            canvas = FigureCanvasTkAgg(fig, 
                               self)   
            canvas.draw() 
            canvas.get_tk_widget().pack() 
  
            toolbar = NavigationToolbar2Tk(canvas, 
                                   self) 
            toolbar.update() 
            canvas.get_tk_widget().pack() 

        self.title("Données")
        self.geometry('500x200')
        self['bg']='grey'

        self.InvestLabel = Label(self, text = "Quel est l'investissement maximal souhaité?")
        self.InvestLabel.config(bg="grey")
        self.InvestLabel.pack()

        max_invest = DoubleVar()
        self.saisie = Entry(self, textvariable = max_invest, width = 10)
        self.saisie.config(bg="grey")
        self.saisie.pack()
        
        self.ReturnLabel = Label(self, text = "Quel est le rendement souhaité ? Si vous ne voulez pas le renseigner rentrez 0")
        self.ReturnLabel.config(bg="grey")
        self.ReturnLabel.pack()

        expected_return = DoubleVar()
        self.saisie2 = Entry(self,textvariable = expected_return, width = 10,)
        self.saisie2.config(bg="grey")
        self.saisie2.pack()
        
        self.VolaLabel = Label(self, text = "Quel est la volatilité souhaitée ? Si vous ne voulez pas le renseigner rentrez 0")
        self.VolaLabel.config(bg="grey")
        self.VolaLabel.pack()

        expected_std = DoubleVar()
        self.saisie3 = Entry(self, textvariable =expected_std, width = 10)
        self.saisie3.config(bg="grey")
        self.saisie3.pack()

        self.bouton = Button(self, text = "VALIDER", width=8, command= getEntry)
        self.bouton.pack()

        self.bouton1 = Button(self, text = "CALCULER", width=8)
        self.bouton1['command']=self.button_clicked
        self.bouton1.pack()

        #plot_button = Button(self, 
        #            #command = plot,
        #             height = 2, 
        #             width = 10, 
        #            text = "Plot") 
        #plot_button.pack() 

        

    def button_clicked(self):

    
        #Connexion a la base de donnée
        connection = Connexion('pi2','root','Leo20-Esilv')
        connection.initialisation()

        #Date de création du portefeuille
        date_1 = "2017-01-05"
        date_2 = "2017-12-29"

        #print("Si vous ne souhaitez pas renseigner de volatilité ou de rendement à atteindre entrez : 0")

        #Valeur Max de l'investissement
        #max_invest = float(input("Quel est le montant que vous souhaitez investir ? : "))
        #max_invest = 300000
    
        #Valeur visée pour le rendement et la volatilitée
        #expected_return = float(input("Quel rendement souhaitez vous atteindre ? : "))
        #expected_std = float(input("Quelle volatilité souhaitez vous atteindre ? : "))
    
        #Nombre de portefeuilles par population
        nb_portefeuils = 5
        Generation_max = 5

        #Creation des différents actifs
        list_asset_with_value = []
        list_asset = Actifs.creationActifs(connection)

        #Associe une valeur a chaque actif
        for asset in list_asset:
                list_asset_with_value.append(asset.Valeur_Actifs(date_1,date_2,connection))

        #Creation de la population initiale
        pop = Population([])
        pop.creation_population(list_asset_with_value,self.max_invest,nb_portefeuils,date_1,date_2,connection)
        print(pop.__repr__())

        #Appel de l'algo Génétique
        algoG = AlgoG(pop,Generation_max).algorihtme_genetique(list_asset_with_value,self.max_invest,self.expected_return, self.expected_std,date_1,date_2,connection)

        showinfo(title='Portefeuille final',
                 message=algoG.__repr__())
        #print('\nPortefeuille final :\n'+algoG.__repr__())
        #print('\n', algoG.liste_Actifs.__str__())

        connection.close_connection()

if __name__ == "__main__":
    app = Interface()
    app.mainloop()
