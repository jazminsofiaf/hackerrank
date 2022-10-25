#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryChildren' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY packets
#

def angryChildren(k, packets):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    packets = []

    for _ in range(n):
        packets_item = int(input().strip())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()
