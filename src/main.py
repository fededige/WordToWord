import time
import networkx as nx

from src import constants
from src.preprocessingDictionary import buildGraph
from src.utils import read_file, r1, r2, r3, r4


def checkInput(word, dict_path, alpha_path):
    words = set(read_file(dict_path))
    alphabet = set(read_file(alpha_path))
    node_list = []
    if word not in words:
        node_list = r1(word, words, alphabet) + r3(word, words, alphabet) + r4(word, words)
        if len(word) > constants.MAX_LENGTH:
            node_list += r2(word, words)
    return node_list


def main():
    alpha_path = "D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/alfabeto.txt"
    print("Do you want to update dictionary? Y/N")
    mode = input().upper()
    print("Insert name_of_dictionary without .txt (press ENTER to use default)")
    dictionary = input()
    if dictionary == "":
        dictionary = "italungo"
    dict_path = "D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/" + dictionary + ".txt"
    if mode == "Y":
        buildGraph(dictionary, dict_path, alpha_path)
    elif mode != "N":
        print("input not recognized")
        return
    print("insert starting word")
    start = input()
    print("insert ending word")
    end = input()
    g = nx.read_adjlist("D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/adj_" + dictionary)

    for node in checkInput(start, dict_path, alpha_path):
        print("start")
        g.add_edge(start, node)
    for node in checkInput(end, dict_path, alpha_path):
        print(node)
        g.add_edge(end, node)
    start_time = time.time()
    i = 0
    for path in nx.all_shortest_paths(g, source=start, target=end):
        i += 1
        print(i, ": ", path, "length: ", len(path))
    print("---paths found in: %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
