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


r2_count = 0


def r2(start, end):
    global r2_count
    r2_count += 1
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

    while q:
        if counter == 1:
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
        start = "inizio"
        end = "fine"
    else:
        end = input()
        if end == "":
            end = "fine"

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
    # print("g.has_edge('inizio', 'inizia') == ", g.has_edge("inizio", "inizia"))
    # print("g.has_node('inizia') == ", g.has_node("inizia"))
    # print("g.has_edge('inizia', 'inezia') == ", g.has_edge("inizia", "inezia"))
    # print("g.has_node('inezia') == ", g.has_node("inezia"))
    # print("g.has_edge('inezia', 'inedia') == ", g.has_edge("inezia", "inedia"))
    # print("g.has_node('inedia') == ", g.has_node("inedia"))
    # print("g.has_edge('inedia', 'india') == ", g.has_edge("inedia", "india"))
    # print("g.has_node('india') == ", g.has_node("india"))
    # print("g.has_edge('india', 'invia') == ", g.has_edge("india", "invia"))
    # print("g.has_node('invia') == ", g.has_node("invia"))
    # print("g.has_edge('invia', 'vinai') == ", g.has_edge("invia", "vinai"))
    # print("g.has_node('vinai') == ", g.has_node("vinai"))
    # print("g.has_edge('vinai', 'vini') == ", g.has_edge("vinai", "vini"))
    # print("g.has_node('vini') == ", g.has_node("vini"))
    # print("g.has_edge('vini', 'fini') == ", g.has_edge("vini", "fini"))
    # print("g.has_node('fini') == ", g.has_node("fini"))
    # print("g.has_edge('fini', 'fine') == ", g.has_edge("fini", "fine"))
    # print("g.has_node('fine') == ", g.has_node("fine"))
    # print()
    print("number of paths calculated: ", len(allPaths), ":")
    for p in allPaths:
        print(p, "length: ", len(p))
    print("la regola due è stata usata: ", r2_count)
    # p = nx.dijkstra_path(g, start, end)
    # print(p, "length:", len(p))


words = set(read_file("D:/informatica/anno2023/IUM/italungo.txt"))
alphabet = set(read_file("D:/informatica/anno2023/IUM/alfabeto.txt"))

if __name__ == '__main__':
    main()
    # s = "abcdefg"
    #
    # start_time = time.time()
    # p = list(permutations(s))
    # print(len(p))
    # print("---permutations found in: %s seconds ---" % (time.time() - start_time))
    #
    # start_time = time.time()
    # p = set(permutations(s))
    # print(len(p))
    # print("---permutations found in: %s seconds ---" % (time.time() - start_time))
