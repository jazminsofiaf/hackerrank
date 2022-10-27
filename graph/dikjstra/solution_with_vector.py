#versión sin cola de prioridad #O(V^2)

import heapq as hq
from collections import defaultdict

from collections import defaultdict

# O(n)
def get_min_distance(not_visited, distances):
    node = not_visited[0]
    distance = distances[node]
    for n in not_visited:
        if distances[n] < distance:
            distance = distances[n]
            node = n
    return node, distance


def get_vertices(graph):
    vertices = []
    for i in range(0, len(graph)):
        vertices.append(i)
    return vertices


def bfs(not_visited, graph, father, distances):
    while not_visited:  # Creating loop to visit each node
        node, distance_to_node = get_min_distance(not_visited, distances) #O(v)
        not_visited.remove(node) #O(V)
        for neighbour, weight in enumerate(graph[node]):
            if distance_to_node + weight < distances[neighbour]:
                distances[neighbour] = distance_to_node + weight
                father[neighbour] = node


def dijktra(graph, origin, destination):
    nodes = get_vertices(graph)  # List for non visited nodes.
    father = {}  # map of fathers
    distances = defaultdict(lambda: inf, {})  # distance is a map with infinite default value
    distances[origin] = 0

    # first the cost because the priority queque order by first element
    bfs(nodes, graph, father, distances)

    if destination not in distances.keys():
        print("no path")
        return
    else:
        print("cost: ", distances[destination])
    path = [destination + 1]
    n = destination
    while n != origin:
        if n not in father.keys():
            print("no path")
            return
        else:
            path.insert(0, father[n] + 1)
            n = father[n]
    print("path:", path)


inf = float('inf')
graphMatrix = [[0, 7, 9, inf, inf, 14],
               [7, 0, 10, 15, inf, inf],
               [9, 10, 0, 11, inf, 2],
               [inf, 15, 11, 0, 4, inf],
               [inf, inf, inf, 4, 0, 9],
               [14, inf, 2, inf, 9, 0],
               ]
print("Following is the Dikjstra from V(1) to V(5)")
dijktra(graphMatrix, 0, 4)
