#!/bin/python3

import math
import os
import random
import re
import sys

inf = float('inf')


def create_map(gens, health):
    gen_health_dic = {}
    for i in range(len(gens)):
        gen = gens[i]
        if gen in gen_health_dic:
            gen_health_dic[gen] = gen_health_dic[gen] + health[i]
        else:
            gen_health_dic[gen] = health[i]
    return gen_health_dic


def get_health(gens, health, d):
    print(d)
    total_health = 0
    gen_health_dic = create_map(gens, health)
    print(gen_health_dic)
    for i in range(len(d)):
        for j in range(i, len(d)):
            substring = d[i:j+1]
            print(substring)
            if substring in gen_health_dic:
                total_health = total_health + gen_health_dic[substring]
                print(total_health)

    print()
    return total_health


def get_max_min_healthier(gens, health, input_values):
    min_health = inf
    max_health = 0
    for input_line in input_values:
        first = int(input_line[0])
        last = int(input_line[1])
        d = input_line[2]
        health_sum = get_health(gens[first:last + 1], health[first:last + 1], d)
        if health_sum > max_health:
            max_health = health_sum
        if health_sum < min_health:
            min_health = health_sum
    print(min_health, " ", max_health)


if __name__ == '__main__':
    get_max_min_healthier(['a', 'b', 'c', 'aa', 'd', 'b'], [1, 2, 3, 4, 5, 6],
                          [['1', '5', 'caaab'], ['0', '4', 'xyz'], ['2', '4', 'bcdybc']])

"""
if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())

    values = []

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()
        values.append(first_multiple_input)

    get_max_min_healthier(genes, health, values)
"""
