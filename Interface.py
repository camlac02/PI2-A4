from tkinter import *

fenetre=Tk()
fenetre.title("Risque maximal")

Label = Label(fenetre, text = "Quel est le risque maximal souhaité")
Label.pack()

risk = StringVar()
saisie = Entry(fenetre, textvariable = risk, width = 10)
saisie.pack()

bouton1 = Button(fenetre, text = "CALCULER", width=8)
bouton1.pack()

fenetre.mainloop()