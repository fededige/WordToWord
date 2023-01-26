import time
import networkx as nx

from src.utils import addWord

global g
global alpha_path
global dict_path


def impGraph(dictionary):
    global g
    global alpha_path
    global dict_path
    alpha_path = "../Dictionaries/alfabeto.txt"
    dict_path = "../Dictionaries/" + dictionary + "/" + dictionary + ".txt"
    g = nx.read_adjlist(
        "../Dictionaries/" + dictionary + "/adj_" + dictionary)


def tempAddWord(word):
    global g
    global alpha_path
    global dict_path
    g = addWord(g, word, dict_path, alpha_path)


def compute(start, end):
    global g
    global alpha_path
    global dict_path
    g = addWord(g, start, dict_path, alpha_path)
    g = addWord(g, end, dict_path, alpha_path)
    start_time = time.time()
    i = 0
    result = str()
    paths = nx.all_shortest_paths(g, source=start, target=end)
    elapsedTime = str((time.time() - start_time))
    betterElapseTime = elapsedTime.split(".")[0] + "." + elapsedTime.split(".")[1][0:4]
    for path in paths:
        i += 1
        result += str(i) + ")" + "\n"
        for p in path:
            result += p + "\n"
        result += "length: " + str(len(path)) + "\n"
        result += "\n"
    result += "#" + "--- " + str(i) + " paths found in: " + betterElapseTime + " seconds ---"
    return result
