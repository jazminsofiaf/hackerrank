#!/bin/python3

####### ATENTION NOT VALID FOR HACKER RANK INVALID IMPORT

import math
import os
import random
import re
import sys
from pqdict import PQDict
from collections import defaultdict

inf = float('inf')


# O(E)
def get_neighbors(this_node, edges):
    r = []
    for e in edges:
        node_a = e[0]
        node_b = e[1]
        cost = e[2]
        if node_a == this_node:
            destination_node = node_b
            r.append((destination_node, cost))
        if node_b == this_node:
            destination_node = node_a
            r.append((destination_node, cost))
    return r


#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
# O(log(|v|)*|E|*log(|V|) + |v|) =  O((log(|v|))^2*|E|)
# |E| << |V| => O(log(|v|)^2)
def shortestReach(n, edges, s):
    result = []

    visited = []
    costs_map = defaultdict(lambda: inf, {s: 0})  # distance is a map with infinite default value
    index_pq = PQDict({s: 0})  # Initialize a priority queue with distance as priority
    while index_pq:
        this_node, cost_to_this_node = index_pq.popitem()  # O(log|v|)
        visited.append(this_node)
        for neighbor, cost_from_this_node_to_neighbor in get_neighbors(this_node, edges):  # O(|E|)
            if neighbor in visited:
                continue
            if cost_to_this_node + cost_from_this_node_to_neighbor < costs_map[neighbor]:
                costs_map[neighbor] = cost_to_this_node + cost_from_this_node_to_neighbor
                if neighbor in index_pq:
                    index_pq.updateitem(neighbor, costs_map[neighbor])  # O(log|v|)
                else:
                    index_pq.additem(neighbor, costs_map[neighbor])  # O(log|v|)

    for node in range(1, n + 1):  # O(|v|)
        if node == s:
            continue
        if costs_map[node] == inf:
            result.append(-1)
        else:
            result.append(costs_map[node])
    return result


if __name__ == '__main__':
    print(shortestReach(5, [[1, 2, 5], [1, 3, 15], [2, 3, 6], [3, 4, 2]], 1))
    print(shortestReach(6, [[1, 2, 7], [1, 3, 9], [1, 6, 14],  [2, 3, 10], [2, 4, 15], [3, 4, 11],  [3, 6, 2],  [4, 5, 6],  [5, 6, 9]], 1))

"""    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
"""
