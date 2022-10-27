#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#
def minimumPasses(m, w, p, n):
    # Write your code here

    total_candies = m * w
    passes = 1
    while total_candies < n:
        print(m, " x ", w, "=", m * w, " + ", total_candies, "=", m * w + total_candies)
        passes = passes + 1
        money = total_candies/p
        if money < 1:
            total_candies = total_candies + m * w
            continue
        money = total_candies / p
        while money > 0:
            if m < w:
                m = m + 1
            else:
                w = w + 1
            money = money - 1
            total_candies = total_candies - p
            candies = total_candies + m * w
            if candies >= n:
                break
        total_candies = candies
    return passes


def minimumPasses2(m, w, p, n):
    # Write your code here

    total_candies = m * w
    passes = 1
    while total_candies < n:
        passes = passes + 1
        money = int(total_candies/p)
        if money < 1:
            print(m, " x ", w, "=", m * w, " + ", total_candies, "=", m * w + total_candies)
            print("\n")
            total_candies = total_candies + m * w
            continue
        money = int(total_candies / p)
        min_spent = int(money / 2)
        max_spent = int(money / 2) + int(money % 2)
        candies_left = total_candies - p * money
        if m < w:
            m = m + max_spent
            w = w + min_spent
        else:
            w = w + max_spent
            m = m + min_spent
        candies = candies_left + m * w
        print(m, " x ", w, "=", m * w, " + ", candies_left, "=", m * w + candies_left)
        print("\n")
        total_candies = candies
    return passes


if __name__ == '__main__':
    #print(minimumPasses(5184889632, 5184889632, 20, 10000))
    #print(minimumPasses(3, 1, 2, 12))
    #print(minimumPasses(1, 2, 1, 60))
    print(minimumPasses(1, 1, 6, 45))
    #print(minimumPasses(1, 1, 1000000000000, 1000000000000))



'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
'''
