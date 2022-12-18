import time
from itertools import permutations
import networkx as nx
import constants


def read_file(path):
    with open(path, "r") as f:
        lines = f.read().split()
    return lines


def r1(start):
    words_r1 = list()
    for pos in range(len(start)):
        start_list = list(start)
        for letter in alphabet:
            start_list[pos] = letter
            temp = "".join(start_list)
            if (temp in words) & (temp != start):
                if temp not in words_r1:
                    words_r1.append(temp)
    return words_r1


def r2(start):
    words_r2 = list()
    for perm in permutations(start):
        temp = "".join(perm)
        if (temp in words) & (temp != start):
            if temp not in words_r2:
                words_r2.append(temp)
    return words_r2


def r3(start):
    words_r3 = list()
    for pos in range(len(start) + 1):
        start_list = list(start)
        for letter in alphabet:
            start_list.insert(pos, letter)
            temp = "".join(start_list)
            if (temp in words) & (temp != start):
                if temp not in words_r3:
                    words_r3.append(temp)
            start_list.pop(pos)
    return words_r3


def r4(start):
    words_r4 = list()
    for pos in range(len(start)):
        start_list = list(start)
        letter = start_list.pop(pos)
        temp = "".join(start_list)
        if (temp in words) & (temp != start):
            if temp not in words_r4:
                words_r4.append(temp)
        start_list.insert(pos, letter)
    return words_r4


words = set()
alphabet = set()


def buildGraph(name, dict_path, alph_path):
    global words
    global alphabet
    words = set(read_file(dict_path))
    dictionary = list(read_file(dict_path))
    alphabet = set(read_file(alph_path))
    g = nx.Graph()
    start_time = time.time()
    for p in dictionary:
        g.add_node(p)
        node_list = r1(p) + r3(p) + r4(p)
        if len(p) < constants.MAX_LENGTH:
            node_list += r2(p)
        for n in node_list:
            g.add_edge(p, n)
    print("---building graph time: %s seconds ---" % (time.time() - start_time))
    nx.write_adjlist(g, "adj_" + name)
