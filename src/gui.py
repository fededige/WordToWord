import os
from tkinter import ttk, DISABLED, NORMAL
import tkinter as tk

import networkx as nx

from calcoloPercorso import compute




def onClick(start, end, text, lbl, dictionary):
    text.config(state=NORMAL)
    text.delete('1.0', tk.END)
    try:
        res = compute(start, end, dictionary)
    except nx.NetworkXException:
        res = "no path between " + start + " e " + end + "#---"
    text.insert(tk.END, res.split("#")[0])
    lbl.config(text=res.split("#")[1])
    text.config(state=DISABLED)


def changeDictionary(variable, label):
    global dictionary
    dictionary = variable
    label.config(text="Dictionary: " + dictionary)
    print(dictionary)


def main(window):
    global dictionary
    dictionary = "words_italian"
    window.title("WordToWord")
    window.geometry("800x600")
    tabControl = ttk.Notebook(window)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text="Paths")
    tabControl.add(tab2, text="Dictionary")
    tabControl.pack(expand=1, fill="both")

    startLabel = tk.Label(tab1, text="Start:", font=("Arial", 15))
    startLabel.place(x=5 + 250, y=10)
    startInput = tk.Text(tab1, width=20, height=1.2, font=("Helvetica", 15))
    startInput.place(x=60 + 250, y=10)

    endLabel = tk.Label(tab1, text="End:", font=("Arial", 15))
    endLabel.place(x=5 + 250, y=50)
    endInput = tk.Text(tab1, width=20, height=1.2, font=("Helvetica", 15))
    endInput.place(x=60 + 250, y=50)

    textArea = tk.Text(tab1, width=86, height=20, font=("Arial", 13), bd=2)
    textArea.place(x=5, y=140)

    lblTime = tk.Label(tab1, text="", font=("Arial", 15))
    lblTime.place(x=5, y=530)

    separator = ttk.Separator(tab1, orient='vertical')
    separator.place(x=400, y=526, height=50)

    lblDictionary = tk.Label(tab1, text="Dictionary: " + dictionary, font=("Arial", 15))
    lblDictionary.place(x=410, y=530)

    button = tk.Button(tab1, text="Find!", font=("Arial", 15),
                       command=lambda: onClick(startInput.get("1.0", "end-1c"), endInput.get("1.0", "end-1c"),
                                               textArea,
                                               lblTime, dictionary))
    button.place(x=370, y=90)

    options = next(os.walk("D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/Dictionaries"))[1]
    var = tk.StringVar(root)
    var.set(options[0])  # default value
    w = tk.OptionMenu(tab2, var, *options)
    w.place(x=240, y=50)

    lblTab2 = tk.Label(tab2, text="Choose dictionary:", font=("Arial", 15))
    lblTab2.place(x=50, y=50)
    button2 = tk.Button(tab2, text="Change!", font=("Arial", 15),
                        command=lambda: changeDictionary(var.get(), lblDictionary))
    button2.place(x=50, y=90)

    separator2 = ttk.Separator(tab2, orient="horizontal")
    separator2.place(x=0, y=250, width=800)

    wordLabel = tk.Label(tab2, text="Aggiungi parola: ", font=("Arial", 15))
    wordLabel.place(x=50, y=260)
    wordInput = tk.Text(tab2, width=20, height=1.2, font=("Helvetica", 15))
    wordInput.place(x=200, y=260)
    button3 = tk.Button(tab2, text="Add!", font=("Arial", 15),
                        command=lambda: changeDictionary(var.get(), lblDictionary))
    button3.place(x=50, y=90)


dictionary = str()
if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    root.mainloop()
