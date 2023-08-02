#!/bin/python3

import math
import os
import random
import re
import sys


def countWaysToColorHouses(n):
    MOD = 10**9 + 7
    dp = [[0, 0] for _ in range(n+1)]
    dp[1][0] = 3
    dp[1][1] = 3

    for i in range(2, n//2 + 1):
        dp[i][0] = (2*dp[i-1][0] + dp[i-1][1]) % MOD
        dp[i][1] = (dp[i-1][0] + 2*dp[i-1][1]) % MOD

    return (dp[n//2][0] + dp[n//2][1]) % MOD
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = countWaysToColorHouses(n)

    fptr.write(str(result) + '\n')

    fptr.close()
