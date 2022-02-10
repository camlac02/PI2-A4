from tkinter import *

fenetre=Tk()
fenetre.title("Risque maximal")

Label = Label(fenetre, texte = "Quel est le risque maximal souhaité")
Label.pack()

risk = StringVar()
risk.set("0.1")
saisie = Entry(fenetre, textevariable = risk, width = 10)
saisie.pack()

bouton1 = Button(fenetre, texte = "CALCULER", width=8)
bouton1.pack()

fenetre.mainloop()