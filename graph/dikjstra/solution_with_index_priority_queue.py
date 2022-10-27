from collections import defaultdict
from pqdict import PQDict

def bfs_matrix_graph(visited, graph, index_pq, father, distances):  # function for BFS
    while len(index_pq) > 0:  # Creating loop to visit each node
        node, distance_to_node = index_pq.popitem()
        visited.append(node)
        for neighbour, weight in enumerate(graph[node]):
            if neighbour not in visited:
                if distance_to_node + weight < distances[neighbour]:
                    distances[neighbour] = distance_to_node + weight
                    father[neighbour] = node
                    if neighbour in index_pq:
                        index_pq.updateitem(neighbour, distances[neighbour])
                    else:
                        index_pq.additem(neighbour, distances[neighbour])


def dijktra_with_priority_queue_matrix_graph(graph, origin, destination):
    visited = []  # List for visited nodes.
    father = {}  # map of fathers
    distances = defaultdict(lambda: inf, {origin: 0})  # distance is a map with infinite default value
    index_pq = PQDict({origin: 0})  # Initialize a priority queue with distance as priority
    bfs_matrix_graph(visited, graph, index_pq, father, distances)

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
print("Following is the Dikjstra  with priority queue from V(1) to V(5)")
dijktra_with_priority_queue_matrix_graph(graphMatrix, 0, 4)  # function calling
