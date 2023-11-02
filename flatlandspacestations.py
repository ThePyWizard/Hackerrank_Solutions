#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    prev_st=c[0]
    max_dist=c[0]
    for i in range(1,len(c)):
        current_st=c[i]
        dist=(current_st-prev_st)//2
        max_dist=max(max_dist,dist)
        prev_st=current_st
    max_dist=max(max_dist,n-1-prev_st)
    return max_dist
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
