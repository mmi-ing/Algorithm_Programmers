#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def programmerStrings(s):
    target = Counter("programmer")
    start_count, end_count = Counter(), Counter()
    start_index, end_index = 0, len(s) - 1
    
    while start_index < len(s):
        start_count[s[start_index]] += 1
        if start_count & target == target:
            break
        start_index += 1

    while end_index >= 0:
        end_count[s[end_index]] += 1
        if end_count & target == target:
            break
        end_index -= 1

    return end_index - start_index - 1

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = programmerStrings(s)

    fptr.write(str(result) + '\n')

    fptr.close()
