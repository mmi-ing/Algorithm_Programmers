#!/bin/python3

import math
import os
import random
import re
import sys


def findLargestSquareSize(samples):
    n = len(samples)
    dp = [[0]*n for _ in range(n)]
    largest_size = 0

    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = samples[i][j]
            elif samples[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

            largest_size = max(largest_size, dp[i][j])

    return largest_size
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    samples_rows = int(input().strip())
    samples_columns = int(input().strip())

    samples = []

    for _ in range(samples_rows):
        samples.append(list(map(int, input().rstrip().split())))

    result = findLargestSquareSize(samples)

    fptr.write(str(result) + '\n')

    fptr.close()
