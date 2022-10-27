import heapq as hq
from collections import defaultdict


def bfs_dic_graph(visited, graph, pQuque, father, distances):  # function for BFS
    while pQuque:  # Creating loop to visit each node
        distance_to_node, node = hq.heappop(pQuque)
        visited.append(node)
        for neighbour in graph[node]:
            weight = graph[node][neighbour]
            if neighbour not in visited:
                if distance_to_node + weight < distances[neighbour]:
                    distances[neighbour] = distance_to_node + weight
                    father[neighbour] = node
                    hq.heappush(pQuque, (distances[neighbour], neighbour))


def dijktra_with_priority_queue_dic_graph(graph, origin, destination):
    visited = []  # List for visited nodes.
    father = {}  # map of fathers
    distances = defaultdict(lambda: inf, {})  # distance is a map with infinite default value
    distances[origin] = 0
    pQuque = []  # Initialize a priority queue
    hq.heappush(pQuque,
                (distances[origin], origin))  # first the cost because the priority queque order by first element
    bfs_dic_graph(visited, graph, pQuque, father, distances)

    if destination not in distances.keys():
        print("no path")
    else:
        print("cost: ", distances[destination])
    path = [destination]
    n = destination
    while n != origin:
        if n not in father.keys():
            print("no path")
        else:
            path.insert(0, father[n])
            n = father[n]
    print("path:", path)

graphDic = {1: {1: 0, 2: 7, 3: 9, 6: 14},
            2: {1: 7, 2: 0, 3: 10, 4: 15},
            3: {1: 9, 2: 10, 3: 0, 4: 11, 6: 2},
            4: {2: 15, 3: 11, 4: 0, 5: 4},
            5: {4: 5, 5: 0, 6: 9},
            6: {1: 14, 3: 2, 5: 9, 6: 0}}
print("Following is the Dikjstra  with priority queue from V(1) to V(5)")
dijktra_with_priority_queue_dic_graph(graphDic, 1, 5)  # function calling

