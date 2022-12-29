import os
from tkinter import ttk, DISABLED, NORMAL, END, messagebox
import tkinter as tk

import networkx as nx

from calcoloPercorso import compute, impGraph, tempAddWord
from src.preprocessingDictionary import buildGraph


def onClick(start, end, text, lbl):
    text.config(state=NORMAL)
    text.delete('1.0', END)
    try:
        res = compute(start, end, dictionary)
    except nx.NetworkXException:
        res = "no path between " + start + " and " + end + "#---"
    text.insert(END, res.split("#")[0])
    lbl.config(text=res.split("#")[1])
    text.config(state=DISABLED)


def changeDictionary(variable, label, label2):
    global dictionary
    if os.path.exists("D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/Dictionaries/" + variable + "/adj_" + variable):
        dictionary = variable
        label.config(text="Dictionary: " + dictionary)
        label2.config(text="Dictionary: " + dictionary)
        impGraph(dictionary)
        return
    answer = messagebox.askyesno("Question", "The dictionary chose needs to be preprocessed (it could take a lot of "
                                             "time)")
    if answer:
        dictionary = variable
        buildGraph(dictionary)
        label.config(text="Dictionary: " + dictionary)
        label2.config(text="Dictionary: " + dictionary)
        impGraph(dictionary)
        return


def addWordToGraph(text):
    tempAddWord(text.get("1.0", "end-1c"))
    text.delete('1.0', END)


def main(window):
    global dictionary
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

    lblDictionary2 = tk.Label(tab2, text="Dictionary: " + dictionary, font=("Arial", 15))
    lblDictionary2.place(x=410, y=530)

    button = tk.Button(tab1, text="Find!", font=("Arial", 15),
                       command=lambda: onClick(startInput.get("1.0", "end-1c"), endInput.get("1.0", "end-1c"),
                                               textArea,
                                               lblTime))
    button.place(x=370, y=90)

    options = next(os.walk("D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/Dictionaries"))[1]
    var = tk.StringVar(root)
    var.set(options[0])  # default value
    w = tk.OptionMenu(tab2, var, *options)
    w.place(x=240, y=50)

    lblTab2 = tk.Label(tab2, text="Choose dictionary:", font=("Arial", 15))
    lblTab2.place(x=50, y=50)
    button2 = tk.Button(tab2, text="Change!", font=("Arial", 15),
                        command=lambda: changeDictionary(var.get(), lblDictionary, lblDictionary2))
    button2.place(x=50, y=90)

    separator2 = ttk.Separator(tab2, orient="horizontal")
    separator2.place(x=0, y=250, width=800)

    wordLabel = tk.Label(tab2, text="Add word: ", font=("Arial", 15))
    wordLabel.place(x=50, y=260)
    wordInput = tk.Text(tab2, width=20, height=1.2, font=("Helvetica", 15))
    wordInput.place(x=200, y=260)
    button3 = tk.Button(tab2, text="Add!", font=("Arial", 15),
                        command=lambda: addWordToGraph(wordInput))
    button3.place(x=50, y=300)

    separator = ttk.Separator(tab2, orient='vertical')
    separator.place(x=400, y=526, height=50)



dictionary = "words_italian"
if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    impGraph(dictionary)
    root.mainloop()
