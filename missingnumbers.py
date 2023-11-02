#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    count_a={}
    count_b={}
    for i in arr:
        count_a[i]=count_a.get(i,0)+1
    for i in brr:
        count_b[i]=count_b.get(i,0)+1
    missing=[]
    uni=set(arr+brr)
    for i in uni:
        count_d=count_b.get(i,0)-count_a.get(i,0)
        if count_d>0 and count_d<=100:
            missing.append(i)
    missing.sort()
    return missing


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
