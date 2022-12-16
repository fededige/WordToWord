import time
import networkx as nx


def read_file(path):
    with open(path, "r") as f:
        lines = f.read().split()
    return lines


def foo():
    print("inserisci inizio e fine")
    start = input()
    end = input()
    g = nx.read_adjlist("D:/informatica/anno2023/IUM/adj_10")
    start_time = time.time()
    i = 0
    for path in nx.all_shortest_paths(g, source=start, target=end):
        i += 1
        print(i, ": ", path)
    print("---paths found in: %s seconds ---" % (time.time() - start_time))


words = set(read_file("D:/informatica/anno2023/IUM/italungo.txt"))
alphabet = set(read_file("D:/informatica/anno2023/IUM/alfabeto.txt"))

if __name__ == '__main__':
    foo()