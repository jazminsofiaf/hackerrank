#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

inf = float('inf')

# O(V)
def get_nearest(not_visited, costs_map):
    node = not_visited[0]
    cost = costs_map[node]
    for this_node in not_visited: 
        if costs_map[this_node] < cost:
            node = this_node
            cost = costs_map[this_node]
    return node, cost


# O(E)
def get_neighbors(this_node, edges):
    r = []
    for e in edges:
        node_a = e[0]
        node_b= e[1]
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
#
# O(|V|*(|V|+|E|)) as E is always < E
# O(|V|^2)
def shortestReach(n, edges, s):
    result = []

    not_visited = [*range(1, n + 1)]
    father = {}
    costs_map = defaultdict(lambda: inf, {})
    costs_map[s] = 0

    while not_visited:# O(V)
        this_node, cost_to_this_node = get_nearest(not_visited, costs_map)# O(V)
        not_visited.remove(this_node)
        for neighbor, cost_from_this_node_to_neighbor in get_neighbors(this_node, edges):# O(E)
            if cost_to_this_node + cost_from_this_node_to_neighbor < costs_map[neighbor]:
                costs_map[neighbor] = cost_to_this_node + cost_from_this_node_to_neighbor
                father[neighbor] = this_node

    for node in range(1, n + 1):
        if node == s:
            continue
        if costs_map[node] == inf:
            result.append(-1)
        else:
            result.append(costs_map[node])
    return result


if __name__ == '__main__':
    print(shortestReach(5, [[1, 2, 5],[1, 3, 15], [2, 3, 6], [3, 4, 2]], 1))


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