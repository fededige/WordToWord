import time
import networkx as nx
import constants
from src.utils import read_file, r3, r1, r4, r2


def buildGraph(name):
    alpha_path = "D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/Dictionaries/alfabeto.txt"
    dict_path = "D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/Dictionaries/" + name + "/" + name + ".txt"
    words = set(read_file(dict_path))
    dictionary = list(read_file(dict_path))
    alphabet = set(read_file(alpha_path))
    g = nx.Graph()
    start_time = time.time()
    for p in dictionary:
        g.add_node(p)
        node_list = r1(p, words, alphabet) + r3(p, words, alphabet) + r4(p, words)
        if len(p) < constants.MAX_LENGTH:
            node_list += r2(p, words)
        for n in node_list:
            g.add_edge(p, n)
    print("---building graph time: %s seconds ---" % (time.time() - start_time))
    nx.write_adjlist(g, "D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/Dictionaries/" + name + "/" + "adj_" + name)
