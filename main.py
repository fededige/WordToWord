import time
import networkx as nx
import preprocessingDictionary


def read_file(path):
    with open(path, "r") as f:
        lines = f.read().split()
    return lines


# def checkInput(g, start, end):
#     if start not in words:
#         start_nodes = r1(start) + r2(start) + r3(start) + r4(start)
#         for n in start_nodes:
#             g.add_edge(start, n)
#     if end not in words:
#         end_nodes = r1(end) + r2(end) + r3(end) + r4(end)
#         for n in end_nodes:
#             g.add_edge(end, n)
#     return g


# def buildGraph(name):
#     fullGraph = nx.Graph()
#     build_time = time.time()
#     for singleWord in tempWords:
#         fullGraph.add_node(singleWord)
#         node_list = r1(singleWord) + r3(singleWord) + r4(singleWord)
#         if len(singleWord) < constants.MAX_LENGTH:
#             node_list += r2(singleWord)
#         for n in node_list:
#             fullGraph.add_edge(singleWord, n)
#     print("---building graph time: %s seconds ---" % (time.time() - build_time))
#     nx.write_adjlist(fullGraph, "adj_" + name)


def main():
    alpha_path = "D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/alfabeto.txt"
    print("Do you want to update dictionary? Y/N")
    mode = input().upper()
    if mode == "Y":
        print("Insert name_of_dictionary (that you already put in "
              "'D:/informatica/anno2023/IUM/PycharmProjects/WordToWord')")
        dictionary = input()
        dict_path = "D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/" + dictionary + ".txt"
        preprocessingDictionary.buildGraph(dictionary, dict_path, alpha_path)
    elif mode == "N":
        print("Insert name_of_dictionary without .txt (press ENTER to use default)")
        dictionary = input()
        if dictionary == "":
            dictionary = "italungo"
    else:
        print("input not recognized")
        return
    print("inserisci parola da da cui partire")
    start = input()
    print("inserisci parola a cui arrivare")
    end = input()

    g = nx.read_adjlist("D:/informatica/anno2023/IUM/PycharmProjects/WordToWord/adj_" + dictionary)

    # g = checkInput(g, start, end) #to be completed (maybe write an utils.py with all rules

    start_time = time.time()
    i = 0
    for path in nx.all_shortest_paths(g, source=start, target=end):
        i += 1
        print(i, ": ", path, "length: ", len(path))
    print("---paths found in: %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
