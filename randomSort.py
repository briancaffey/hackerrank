x = [1,0,3,9,2]
import random, math

def sort_num(arr):
    n = length(arr)
    for i in range(1, n-1)[:-1]:
        pick = math.floor((i+1)*rand())
        temp = arr[i]
        arr[i] = arr[pick]
        arr[pick] = temp
