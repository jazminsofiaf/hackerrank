from collections import defaultdict


class IndexedMinPQ:
    def __init__(self, N):
        self.N = N
        self.key = [None for i in range(self.N)]
        self.pq = [None for i in range(self.N + 1)]
        self.qp = [None for i in range(self.N)]
        self.total = 0

    def isIndexUsed(self, i):
        assert type(i) is int
        return self.key[i] is not None

    def insert(self, i, key):
        print("inser ",i," ",key)
        assert type(i) is int
        if i >= self.N:
            raise IndexError('index ',i,' is out of the range of IndexedMinPQ ', self.N)
        if self.key[i] is not None:
            raise IndexError('index is already in the IndexedMinPQ.')
        self.total += 1
        self.key[i] = key
        self.pq[self.total] = i
        self.qp[i] = self.total
        self.__swim(self.total)
        print("keys: ",self.key)
        print("pq: ", self.pq)
        print("qp: ",self.qp)
        print("")

    def __swim(self, i):
        parent_i = i // 2

        while parent_i > 0:
            key = self.key[self.pq[i]]
            parent_key = self.key[self.pq[parent_i]]
            if parent_key < key:
                break
            self.pq[i], self.pq[parent_i] = self.pq[parent_i], self.pq[i]
            self.qp[self.pq[i]], self.qp[self.pq[parent_i]] = self.qp[self.pq[parent_i]], self.qp[self.pq[i]]
            i = parent_i
            parent_i = i // 2

    def deleteMin(self):
        if not self.isEmpty():
            out = self.key[self.pq[1]]
            self.key[self.pq[1]] = None
            self.qp[self.pq[1]] = None
            self.pq[1] = self.pq[self.total]
            self.qp[self.pq[1]] = 1
            self.pq[self.total] = None
            self.total -= 1
            self.__sink(1)
            return out
        raise IndexError('IndexedMinPQ is Empty')

    def __sink(self, i):
        child_i = i * 2
        if child_i <= self.total:
            key = self.key[self.pq[i]]
            child_key = self.key[self.pq[child_i]]
            other_child = child_i + 1
            if other_child <= self.total:
                other_child_key = self.key[self.pq[other_child]]
                if other_child_key < child_key:
                    child_i = other_child
                    child_key = other_child_key
            if child_key < key:
                self.pq[i], self.pq[child_i] = self.pq[child_i], self.pq[i]
                self.qp[self.pq[i]], self.qp[self.pq[child_i]] = self.qp[self.pq[child_i]], self.qp[self.pq[i]]
                self.__sink(child_i)

    def isEmpty(self):
        return self.total == 0

    def decreaseKey(self, i, key):
        if i < 0 or i > self.N:
            raise IndexError('index i is not in the range')
        if self.key[i] is None:
            raise IndexError('index i is not in the IndexedMinPQ')
        assert type(i) is int
        assert key < self.key[i]
        self.key[i] = key
        self.__swim(self.qp[i])

    def increaseKey(self, i, key):
        if i < 0 or i > self.N:
            raise IndexError('index i is not in the range')
        if self.key[i] is None:
            raise IndexError('index i is not in the IndexedMinPQ')
        assert type(i) is int
        assert key > self.key[i]
        self.key[i] = key
        self.__sink(self.qp[i])


###########################################################

def bfs_matrix_graph(visited, graph, index_pq, father, distances):  # function for BFS
    while not index_pq.isEmpty():  # Creating loop to visit each node
        distance_to_node, node = index_pq.deleteMin()
        visited.append(node)
        for neighbour, weight in enumerate(graph[node]):
            if neighbour not in visited:
                if distance_to_node + weight < distances[neighbour]:
                    distances[neighbour] = distance_to_node + weight
                    father[neighbour] = node
                    if index_pq.isIndexUsed(neighbour):
                        index_pq.decreaseKey(neighbour, (distances[neighbour], neighbour))
                    else:
                        index_pq.insert(neighbour, (distances[neighbour], neighbour))


def dijktra_with_priority_queue_matrix_graph(graph, origin, destination):
    visited = []  # List for visited nodes.
    father = {}  # map of fathers
    distances = defaultdict(lambda: inf, {})  # distance is a map with infinite default value
    distances[origin] = 0
    index_pq = IndexedMinPQ(len(graph)+1)  # Initialize a priority queue
    index_pq.insert(origin, (distances[origin], origin))  # first the cost because the priority queque order by first element
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

