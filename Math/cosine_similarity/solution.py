#!/bin/python3

import math


def get_mag(values_sum):
    return math.sqrt(values_sum)


#
# Complete the 'cosine_similarity' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a_keys
#  2. DOUBLE_ARRAY a_values
#  3. INTEGER_ARRAY b_keys
#  4. DOUBLE_ARRAY b_values
#
def cosine_similarity(a_keys, a_values, b_keys, b_values):
    map_a = {}
    map_b = {}

    sum_square_a = 0
    for i in range(len(a_keys)):  # O(Na)
        map_a[a_keys[i]] = a_values[i]
        sum_square_a = sum_square_a + (a_values[i] ** 2)

    sum_square_b = 0
    for i in range(len(b_keys)):  # O(Nb)
        map_b[b_keys[i]] = b_values[i]
        sum_square_b = sum_square_b + (b_values[i] ** 2)

    total_mul = 0
    for key in map_a:  # O(Na)
        if key not in map_b:
            total_mul = total_mul + 0
        else:
            val_a = map_a[key]
            val_b = map_b[key]
            total_mul = total_mul + (val_a * val_b)

    mag_a = get_mag(sum_square_a)
    mag_b = get_mag(sum_square_b)
    return total_mul / (mag_a * mag_b) # O(2Na+Nb)= O(Na+Nb)


if __name__ == '__main__':
    print(round(cosine_similarity([689944194], [346.932302390659], [689944194], [780.418827561857]), 3))
    print(round(cosine_similarity([0, 1, 3], [3, 2, 5], [0], [1]), 3))
    print(round(cosine_similarity([0, 1, 2, 3, 4], [1, 1, 1, 1, 1], [2, 3, 5, 6], [1, 1, 1, 1]), 3))
