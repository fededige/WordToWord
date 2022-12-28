from tkinter import ttk
import tkinter as tk
from calcoloPercorso import calcola


def onClick(inizio, fine, text, lbl):
    textArea.delete('1.0', tk.END)
    try:
        res = calcola(inizio, fine)
    except Exception:
        res = "no path between " + inizio + " e " + fine + "#---"
    print(res)
    text.insert(tk.END, res.split("#")[0])
    lbl.config(text=res.split("#")[1])


root = tk.Tk()

root.title("WordToWord")
root.geometry("800x600")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Cammini")
tabControl.add(tab2, text="Dizionario")
tabControl.pack(expand=1, fill="both")

lblInizio = tk.Label(tab1, text="Inizio:", font=("Arial", 15))
lblInizio.place(x=5+250, y=10)
inizioInput = tk.Text(tab1, width=20, height=1.2, font=("Helvetica", 15))
inizioInput.place(x=60+250, y=10)

lblFine = tk.Label(tab1, text="Fine:", font=("Arial", 15))
lblFine.place(x=5+250, y=50)
fineInput = tk.Text(tab1, width=20, height=1.2, font=("Helvetica", 15))
fineInput.place(x=60+250, y=50)

textArea = tk.Text(tab1, width=86, height=20, font=("Arial", 13), bd=2)
textArea.place(x=5, y=140)

lblTime = tk.Label(tab1, text="", font=("Arial", 15))
lblTime.place(x=5, y=530)

button = tk.Button(tab1, text="Trova!", font=("Arial", 15),
                   command=lambda: onClick(inizioInput.get("1.0", "end-1c"), fineInput.get("1.0", "end-1c"), textArea,
                                           lblTime))
button.place(x=370, y=90)

# command=lambda: onClick(inizioInput.get("1.0", "end-1c"), fineInput.get("1.0", "end-1c"))
root.mainloop()

# window = Tk()
#
# window.title("Cerca il cammino")
# window.geometry('600x450')
#
# lbl = Label(window, text="Parola inizio", padx=15)
# lbl.grid(column=4, row=3)
# parolaIniz = Entry(window, width=10)
# parolaIniz.grid(column=4, row=5)
#
# lbl2 = Label(window, text="Parola fine", padx=5)
# lbl2.grid(column=8, row=3)
# parolaFin = Entry(window, width=10)
# parolaFin.grid(column=8, row=5)
#
# risultato = scrolledtext.ScrolledText(window, width=50, height=22)
# risultato.grid(column=5, row=15)
# risultato.insert(INSERT, " ")
#
#
# def clicca():
#     resul = parolaIniz.get() + " " + parolaFin.get()
#     risultato.insert(INSERT, " " + calcola(parolaIniz.get(), parolaFin.get()))
#
#
# btn = Button(window, text="Cerca il cammino", command=clicca)
# btn.grid(column=5, row=9)
#
# window.mainloop()
