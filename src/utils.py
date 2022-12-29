from itertools import permutations

from src import constants


def read_file(path):
    with open(path, "r") as f:
        lines = f.read().split()
    return lines


def r1(start, words, alphabet):
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


def r2(start, words):
    words_r2 = list()
    for perm in permutations(start):
        temp = "".join(perm)
        if (temp in words) & (temp != start):
            if temp not in words_r2:
                words_r2.append(temp)
    return words_r2


def r3(start, words, alphabet):
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


def r4(start, words):
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


def computeNode(word, dict_path, alpha_path):
    words = set(read_file(dict_path))
    alphabet = set(read_file(alpha_path))
    node_list = []
    if word not in words:
        node_list = r1(word, words, alphabet) + r3(word, words, alphabet) + r4(word, words)
        if len(word) < constants.MAX_LENGTH:
            node_list += r2(word, words)
    return node_list


def addWord(g, word, dict_path, alpha_path):
    if word not in g:
        for node in computeNode(word, dict_path, alpha_path):
            g.add_edge(word, node)
    return g
