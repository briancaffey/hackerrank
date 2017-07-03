#!/bin/python

import sys

def super_reduced_string(s):
    for num in range(len(s)-1):
        if s[num] == s[num+1]:
            s_ = s[:num] + s[num+2:]
            return super_reduced_string(s_)

    if len(s)>0:
        return s
    else:
        return "Empty String"

s = raw_input().strip()
result = super_reduced_string(s)
print(result)
