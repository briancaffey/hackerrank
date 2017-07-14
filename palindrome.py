def pal(string):
    length = len(string)
    if length % 2 == 0:
        for i in range(length/2 - 1):
            if string[i] != string[length-1-i]:
                return False
        return True
    else:
        for i in range(length/2):
            if string[i] != string[length-1-i]:
                return False
        return True

print 'abddba ' + str(pal('abddba'))

print 'abcba ' + str(pal('abcba'))

print 'abdiuiedri ' + str(pal('abdiuiedri'))
