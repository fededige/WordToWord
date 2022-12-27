import time
import networkx as nx

from src import constants
from src.preprocessingDictionary import buildGraph
from src.utils import read_file, r1, r2, r3, r4


def addWord(word, dict_path, alpha_path):
    words = set(read_file(dict_path))
    alphabet = set(read_file(alpha_path))
    node_list = []
    if word not in words:
        node_list = r1(word, words, alphabet) + r3(word, words, alphabet) + r4(word, words)
        if len(word) > constants.MAX_LENGTH:
            node_list += r2(word, words)
    return node_list


def calcola(start, end):
    alpha_path = "D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/Dictionaries/alfabeto.txt"
    print("Do you want to update dictionary? Y/N")
    mode = input().upper()
    print("Insert name_of_dictionary without .txt (press ENTER to use default)")
    dictionary = input()
    if dictionary == "":
        dictionary = "italungo"
    dict_path = "D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/Dictionaries/" + dictionary + "/" + dictionary + ".txt"
    if mode == "Y":
        buildGraph(dictionary, dict_path, alpha_path)
    elif mode != "N":
        print("input not recognized")
        return
    pause = input()
    print(pause)
    g = nx.read_adjlist("D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/Dictionaries/" + dictionary + "/adj_" + dictionary)

    for node in addWord(start, dict_path, alpha_path):
        g.add_edge(start, node)
    for node in addWord(end, dict_path, alpha_path):
        g.add_edge(end, node)
    start_time = time.time()
    i = 0
    stringa = str()
    for path in nx.all_shortest_paths(g, source=start, target=end):
        i += 1
        stringa += str(i) + ": " + str(path) + "length: " + str(len(path)) + "\n"
    stringa += ("---paths found in: %s seconds ---" % (time.time() - start_time))
    return stringa

# if __name__ == '__main__':
#     main()
