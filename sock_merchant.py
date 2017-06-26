#!/bin/python

import sys

def sockMerchant(n, ar):
    # Complete this function
    count = {x:0 for x in ar}
    for sock in ar:
        count[sock] += 1


    total_pairs = 0
    for key, val in count.items():
        if val == 0 or val == 1:
            pass
        if val % 2 == 0:
            total_pairs += val/2
        else:
            total_pairs += (val-1)/2
    return total_pairs

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
