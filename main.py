import time
import networkx as nx
from itertools import permutations
from queue import Queue


def read_file(path):
    with open(path, "r") as f:
        lines = f.read().split()
    return lines


def r1(start, end):
    words_r1 = list()
    for pos in range(len(start)):
        start_list = list(start)
        for letter in alphabet:
            start_list[pos] = letter
            temp = "".join(start_list)
            if ((temp in words) & (temp != start)) | (temp == end):
                if temp not in words_r1:
                    words_r1.append(temp)
    return words_r1


def r2(start, end):
    words_r2 = list()
    for perm in permutations(start):
        temp = "".join(perm)
        if ((temp in words) & (temp != start)) | (temp == end):
            if temp not in words_r2:
                words_r2.append(temp)
    return words_r2


def r3(start, end):
    words_r3 = list()
    for pos in range(len(start) + 1):
        start_list = list(start)
        for letter in alphabet:
            start_list.insert(pos, letter)
            temp = "".join(start_list)
            if ((temp in words) & (temp != start)) | (temp == end):
                if temp not in words_r3:
                    words_r3.append(temp)
            start_list.pop(pos)
    return words_r3


def r4(start, end):
    words_r4 = list()
    for pos in range(len(start)):
        start_list = list(start)
        letter = start_list.pop(pos)
        temp = "".join(start_list)
        if ((temp in words) & (temp != start)) | (temp == end):
            if temp not in words_r4:
                words_r4.append(temp)
        start_list.insert(pos, letter)
    return words_r4


def build_level(g, start, end):
    flag = False
    node_list = r1(start, end) + r3(start, end) + r4(start, end)
    if len(start) == len(end):
        node_list += r2(start, end)
    for node in node_list:
        if not g.has_edge(start, node):
            g.add_edge(start, node)
        if node == end:
            flag = True
    if flag:
        return None
    return node_list


allPaths = list()


def addPath(g, start, end, c):
    global allPaths
    global start_time
    for path in nx.all_shortest_paths(g, source=start, target=end):
        if path not in allPaths:
            print(path)
            allPaths.append(path)
    print("---calculating paths took %s seconds ---" % (time.time() - start_time))


def build_graph(g, start, end):
    level = build_level(g, start, end)
    counter = 0
    if level is None:
        addPath(g, start, end, counter)
        return g
    q = Queue(maxsize=0)
    for n in level:
        if n not in q.queue:
            q.put(n)

    while not q.empty():
        if counter == 3:
            return g
        n = q.get()
        if n != start:
            level = build_level(g, n, end)
            if level is None:
                counter += 1
                addPath(g, start, end, counter)
            else:
                for n in level:
                    if (n not in q.queue) & (len(n) > 3):
                        q.put(n)
    return g


start_time = float()


def main():
    print("insert two words, press enter to use default")
    start = input()
    if start == "":
        start = "ciao"
        end = "piano"
    else:
        end = input()
        if end == "":
            end = "piano"

    g = nx.Graph()
    print("building graph")
    global start_time
    start_time = time.time()
    g = build_graph(g, start, end)
    print()
    print()
    print("_____________________")
    print("---building graph time: %s seconds ---" % (time.time() - start_time))
    print("graph has: " + str(g.number_of_nodes()) + " nodes")
    print("graph has: " + str(g.number_of_edges()) + " edges")
    print("_____________________")
    print()
    print()
    # start_time = time.time()
    # print(nx.dijkstra_path(g, start, end))
    # print("---calculating min path took %s seconds ---" % (time.time() - start_time))
    # start_time = time.time()
    # print([p for p in nx.all_shortest_paths(g, source=start, target=end)])
    # print("---calculating all paths took %s seconds ---" % (time.time() - start_time))


words = set(read_file("D:/informatica/anno2023/IUM/italungo.txt"))
alphabet = set(read_file("D:/informatica/anno2023/IUM/alfabeto.txt"))

if __name__ == '__main__':
    main()
