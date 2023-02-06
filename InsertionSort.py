#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for index in range(n-2,-1,-1):
        while index < n-1 and arr[index] > arr[index + 1]:
            temp = arr[index + 1]
            arr[index + 1] = arr[index]
            print(*(arr))
            arr[index] = temp
            index += 1
    print(*(arr))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
