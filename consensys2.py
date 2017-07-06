#python2

a = [100, 1,1,1,1,1,1,1, 234]

# should be 67 = 69 - 2

# find the largest difference of a[j] - a[i]
# where i < j and a[i] < a[j]

def max_diff(arr):
    small = {'index': -1, 'val': max(arr)}
    big = {'index': 1, 'val': -1}
    diff = -1

    for num, val in enumerate(arr):
        #small
        if num<big['index'] and val<small['val']:
            small['val'] = val
            small['index'] = num

        #large
        if num>small['index'] and val>big['val']:
            big['val'] = val
            big['index'] = num
        #diff
        if big['val'] - small['val'] > diff:
            diff = big['val'] - small['val']

    print diff

max_diff(a)
