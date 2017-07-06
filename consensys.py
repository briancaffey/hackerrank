#python2

test = [1,2, 23, 45, 7,5,5,5,5, 3,3,3,3,1,1,1,5,5,6,7,8,9, 9, 9, 9, 9]
# dic = {1:4, 2:1, 3:1, 5:2, 6:1, 7:1, 8:1}
from collections import defaultdict


def special_sort(test):
    dic = defaultdict(lambda: 0)
    for x in test:
        dic[x] += 1

    final_dic = defaultdict(lambda: [])
    for key, val in dic.items():
        final_dic[val].append(key)

    sorted_keys = sorted(final_dic.keys())

    for x in sorted_keys:
        y = sorted(final_dic[x])
        for _ in y: print (str(_)+'\n')*x,

special_sort(test)
