#!/bin/python3

import math
import os
import random
import re
import sys


def numDuplicates(name, price, weight):
    product_dict = {}
    duplicates = 0

    for i in range(len(name)):
        product_id = (name[i], price[i], weight[i])

        #중복 확인
        if product_id in product_dict:
            duplicates += 1
        else:
            product_dict[product_id] = 1

    return duplicates
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    name_count = int(input().strip())

    name = []

    for _ in range(name_count):
        name_item = input()
        name.append(name_item)

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)

    weight_count = int(input().strip())

    weight = []

    for _ in range(weight_count):
        weight_item = int(input().strip())
        weight.append(weight_item)

    result = numDuplicates(name, price, weight)

    fptr.write(str(result) + '\n')

    fptr.close()
