from tkinter import *
from tkinter import scrolledtext
from main import calcola

window = Tk()

window.title("Cerca il cammino")
window.geometry('600x450')

lbl = Label(window, text="Parola inizio", padx=15)
lbl.grid(column=4, row=3)
parolaIniz = Entry(window, width=10)
parolaIniz.grid(column=4, row=5)

lbl2 = Label(window, text="Parola fine", padx=5)
lbl2.grid(column=8, row=3)
parolaFin = Entry(window, width=10)
parolaFin.grid(column=8, row=5)

risultato = scrolledtext.ScrolledText(window, width=50, height=22)
risultato.grid(column=5, row=15)
risultato.insert(INSERT, " ")


def clicca():
    resul = parolaIniz.get() + " " + parolaFin.get()
    risultato.insert(INSERT, " " + calcola(parolaIniz.get(), parolaFin.get()))


btn = Button(window, text="Cerca il cammino", command=clicca)
btn.grid(column=5, row=9)

window.mainloop()
